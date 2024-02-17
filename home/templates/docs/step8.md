## Django on GCP Cloud Run

To recap, three steps need to be perform to deploy Django App on GCP Cloud Run. 

1. Prep GCP Backend Services
2. Prep Django App to use GCP Backend Services
3. Configure, Build, and Deploy app

Last two steps, we perform the first and second steps. In this step, we will create necessary configuration, build the image, and deploy image on GCP. We should have fully working app on GCP at the end of this step.

## Configure, build, and run migration steps

#### Create secret `django_superuser_password` holding password phrase in Secret Manager

```
echo -n $(cat /dev/urandom | LC_ALL=C tr -dc 'a-zA-Z0-9' | fold -w 30 | head -n 1) | gcloud secrets create django_superuser_password --data-file=-
```

#### Allow service account to access secret
```
gcloud secrets add-iam-policy-binding django_superuser_password \
  --member serviceAccount:${SERVICE_ACCOUNT} \
  --role roles/secretmanager.secretAccessor
```

#### Update your Procfile

```
migrate: python manage.py migrate && python manage.py collectstatic --noinput --clear
createuser: python manage.py createsuperuser --username admin --email noop@example.com --noinput
```

#### Build your application image

```
gcloud builds submit --pack image=${ARTIFACT_REGISTRY}/qr-generator
```

#### Create Cloud Run jobs

* Create a job for the migration
```
gcloud run jobs create qr-migrate \
  --region $REGION \
  --image ${ARTIFACT_REGISTRY}/qr-generator \
  --set-cloudsql-instances ${PROJECT_ID}:${REGION}:gcp-project-id-instance \
  --set-secrets APPLICATION_SETTINGS=application_settings:latest \
  --service-account $SERVICE_ACCOUNT \
  --command migrate
```
* Create a job for the user creation
```
gcloud run jobs create qr-createuser \
  --region $REGION \
  --image ${ARTIFACT_REGISTRY}/qr-generator \
  --set-cloudsql-instances ${PROJECT_ID}:${REGION}:gcp-project-id-instance \
  --set-secrets APPLICATION_SETTINGS=application_settings:latest \
  --set-secrets DJANGO_SUPERUSER_PASSWORD=django_superuser_password:latest \
  --service-account $SERVICE_ACCOUNT \
  --command createuser
```

* Execute Cloud Run jobs

```
gcloud run jobs execute qr-migrate --region $REGION --wait
gcloud run jobs execute qr-createuser --region $REGION --wait
```

* Deploy to Cloud Run

```
gcloud run deploy qr-generator \
  --region $REGION \
  --image ${ARTIFACT_REGISTRY}/qr-generator \
  --set-cloudsql-instances ${PROJECT_ID}:${REGION}:gcp-project-id-instance \
  --set-secrets APPLICATION_SETTINGS=application_settings:latest \
  --service-account $SERVICE_ACCOUNT \
  --allow-unauthenticated
```

Record `Service URL` and set its value as `CLOUDRUN_SERVICE_URL` environment variable

i.e. https://qr-generator-hkqrplzava-uc.a.run.app

To find out the service url using gcp cli, use following command.
```
export CLOUDRUN_SERVICE_URL=$(gcloud run services describe qr-generator \
  --platform managed \
  --region $REGION  \
  --format "value(status.url)")

echo $CLOUDRUN_SERVICE_URL
```

* Configure Cloud Run to fetch `CLOUDRUN_SERVICE_URL` from an environment variable 
```
gcloud run services update qr-generator \
  --region $REGION \
  --update-env-vars CLOUDRUN_SERVICE_URL=$CLOUDRUN_SERVICE_URL
```

### Test App

Visit CLOUD_SERVICE_URL from browser.

### Update image and cloud run service

```
gcloud builds submit --pack image=${ARTIFACT_REGISTRY}/qr-generator
gcloud run jobs execute migrate --region $REGION --wait
gcloud run services update qr-generator \
  --platform managed \
  --region $REGION \
  --image ${ARTIFACT_REGISTRY}/qr-generator
```


### To allow CORS for static resources
Create cors-static.json file and add this.
```
[
    {
      "origin": ["https://*.taralnest.com","https://qr-generator-hkqrplzava-uc.a.run.app","http://127.0.0.1:8000","http://localhost:8000"],
      "method": ["GET","POST"],
      "responseHeader": ["Content-Type"],
      "maxAgeSeconds": 3600
    }
]
```
Be sure to have a correct urls.

```
gcloud storage buckets update gs://gcp-project-id-qr-media --cors-file=cors-static.json

```

## Developing application locally

Finally, in order to keep the application developing and running locally, let's define few local environment variables.

```
export SECRET_KEY=MKKADW05OJcIUEB3u82TYkExB7SCCS6bPZaGl0G7b5EcbFK5Ul
export DATABASE_URL=sqlite:///./qr-generator.db

python manage.py runserver
```
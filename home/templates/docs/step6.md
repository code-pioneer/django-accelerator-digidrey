## Deploy Django on GCP Cloud Run

Three steps need to be perform to deploy Django App on GCP Cloud Run

1. Prep GCP Backend Services
2. Prep Django App to use GCP Backend Services
3. Configure, Build, and Deploy app

#### GCP Deployment Prep Steps

```
export PROJECT_ID=gcp-project-id
export REGION=us-central1
```

#### Set python sdk path 
```
export CLOUDSDK_PYTHON=<project home dir>/venv/bin/python3
```

#### Set/Verify GCP CLI setup and default project
```
gcloud auth list
gcloud config list project
gcloud config set project $PROJECT_ID
```

#### Enable cloud API
```
gcloud services enable \
  run.googleapis.com \
  sql-component.googleapis.com \
  sqladmin.googleapis.com \
  compute.googleapis.com \
  cloudbuild.googleapis.com \
  secretmanager.googleapis.com \
  aiplatform.googleapis.com \
  artifactregistry.googleapis.com
```

#### Create a dedicated service account
```
gcloud iam service-accounts create cloudrun-serviceaccount
```

#### Set service account as environment variable
```
export SERVICE_ACCOUNT=$(gcloud iam service-accounts list \
    --filter cloudrun-serviceaccount --format "value(email)")
```

i.e. cloudrun-serviceaccount@gcp-project-id.iam.gserviceaccount.com

#### Create artifactregistry
```
export ARTIFACT_REGISTRY=${REGION}-docker.pkg.dev/${PROJECT_ID}/containers
```

#### Cloud SQL database

- Name: gcp-project-id-instance
- DB: gcp-project-id-qr
- User: gcp-project-id-qruser

##### Create instance
```
gcloud sql instances create gcp-project-id-instance --project $PROJECT_ID \
  --database-version POSTGRES_14 --tier db-f1-micro --region $REGION
```

##### Create Database
```
gcloud sql databases create gcp-project-id-qr --instance gcp-project-id-instance
```

##### Create user for instance 
```
export DJPASS="$(cat /dev/urandom | LC_ALL=C tr -dc 'a-zA-Z0-9' | fold -w 30 | head -n 1)"
gcloud sql users create gcp-project-id-qruser --instance gcp-project-id-instance --password $DJPASS
```

##### Grant permission
```
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member serviceAccount:${SERVICE_ACCOUNT} \
    --role roles/cloudsql.client
```

##### GCP Bucket setup for static file
Name: gcp-project-id-qr-media
```
export GS_BUCKET_NAME=${PROJECT_ID}-qr-media

gcloud storage buckets create gs://${GS_BUCKET_NAME} --location ${REGION} 

gcloud storage buckets add-iam-policy-binding gs://${GS_BUCKET_NAME} \
    --member serviceAccount:${SERVICE_ACCOUNT} \
    --role roles/storage.admin
```

### Grant Vertex AI permission (optional)
If you are planning to use Vertex AI from your Django app, grant IAM permission

```
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member serviceAccount:${SERVICE_ACCOUNT} \
    --role roles/aiplatform.user
```

### GCP Bucket for file upload setup (optional)
If you planning to add 'file upload function in your app, setup separate upload bucket.

Name: gcp-project-id-qr-upload
```
export GS_BUCKET_NAME_UPLOAD=${PROJECT_ID}-qr-upload

gcloud storage buckets create gs://${GS_BUCKET_NAME_UPLOAD} --location ${REGION} 

gcloud storage buckets add-iam-policy-binding gs://${GS_BUCKET_NAME_UPLOAD} \
    --member serviceAccount:${SERVICE_ACCOUNT} \
    --role roles/storage.admin
```



#### Store configuration as secret
```
echo DATABASE_URL=\"postgres://gcp-project-id-qruser:${DJPASS}@//cloudsql/${PROJECT_ID}:${REGION}:gcp-project-id-instance/gcp-project-id-qr\" > .env
echo GS_BUCKET_NAME=\"${GS_BUCKET_NAME}\" >> .env
echo SECRET_KEY=\"$(cat /dev/urandom | LC_ALL=C tr -dc 'a-zA-Z0-9' | fold -w 50 | head -n 1)\" >> .env
echo DEBUG=True >> .env
```

##### Create secret
```
gcloud secrets create application_settings --data-file .env
```

##### Allow the service account access to this secret
```
gcloud secrets add-iam-policy-binding application_settings \
  --member serviceAccount:${SERVICE_ACCOUNT} --role roles/secretmanager.secretAccessor
```

##### Confirm
```
gcloud secrets versions list application_settings
```
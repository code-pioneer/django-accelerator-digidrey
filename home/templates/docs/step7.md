## Django on GCP Cloud Run

To recap, three steps need to be perform to deploy Django App on GCP Cloud Run. 

1. Prep GCP Backend Services
2. Prep Django App to use GCP Backend Services
3. Configure, Build, and Deploy app

In last step, we perform the first one. In this step, we will prep Django App to be ready to consume services provision in last step.


#### Prep Django Project

##### Move the `settings.py` file, renaming it to `basesettings.py`
```
mv mainapp/settings.py mainapp/basesettings.py
```

##### Create new `settings.py` file
```
touch mainapp/settings.py
```
Add following text in `settings.py`.

```
import io
import os
from urllib.parse import urlparse

import environ

## Import the original settings from each template
from .basesettings import *

## Load the settings from the environment variable
env = environ.Env()
env.read_env(io.StringIO(os.environ.get("APPLICATION_SETTINGS", None)))

## Setting this value from django-environ
SECRET_KEY = env("SECRET_KEY")

## Ensure myproject is added to the installed applications
if "mainapp" not in INSTALLED_APPS:
    INSTALLED_APPS.append("mainapp")

## If defined, add service URL to Django security settings
CLOUDRUN_SERVICE_URL = env("CLOUDRUN_SERVICE_URL", default=None)
if CLOUDRUN_SERVICE_URL:
    ALLOWED_HOSTS = [urlparse(CLOUDRUN_SERVICE_URL).netloc]
    CSRF_TRUSTED_ORIGINS = [CLOUDRUN_SERVICE_URL]
    ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
else:
    ALLOWED_HOSTS = ["*"]

## Default false. True allows default landing pages to be visible
DEBUG = env("DEBUG", default=False)

DB_URL = env("DATABASE_URL", default=None)
if DB_URL:
    DATABASES = {"default": env.db()}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'OPTIONS': {
                    'options': '-c search_path=ragschema'
                },
            'NAME': 'rag', 
            'USER': 'rag_admin', 
            'PASSWORD': 'password123',
            'HOST': '127.0.0.1', 
            'PORT': '5432',
        }
    }

## Define static storage via django-storages[google]
GS_BUCKET_NAME = env("GS_BUCKET_NAME")

# Optional for upload functionality
GS_BUCKET_NAME_UPLOAD = env("GS_BUCKET_NAME_UPLOAD")

STATICFILES_DIRS = []

if GS_BUCKET_NAME:
    DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
    STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
else:
    DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
    STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

GS_DEFAULT_ACL = "publicRead"
```

##### Update Python dependencies

In `requirements.txt`, add following packages.
```
gunicorn
psycopg2-binary
django-storages[google]
django-environ
```
Install packages
```
pip install -r requirements.txt
```

##### Define your application image

Create image definiation file `Procfile`
```
touch Procfile
```

Add following line in the file
```
web: gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 mainapp.wsgi:application

```
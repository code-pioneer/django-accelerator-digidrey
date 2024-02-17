## Add "style" and "authentication"

The goal for this step is to add default theme (look & feel), layout and authentication. This reference implementation use "google" as a identity provider. It is also assumed that you have setup Google oAuth and retrieve 'secret key' and 'client id' information.

#### Install necessary packages 

In requirements.txt file, add following
```
django-allauth==0.60.0
django-markdownx==4.0.7
```

Install the packages
```
pip3 install -r requirements.txt 
```

#### Configure SETTINGS.py

1. Modify following configuration in `main/settings.py`

```
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    ... ...

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'home',
]

MIDDLEWARE = [
    ... ...

    'allauth.account.middleware.AccountMiddleware',
]

TEMPLATES = [
    {
        ... ...

        'DIRS': [os.path.join(BASE_DIR, 'templates'),'/templates'],
        
        ... ...
    },
]

TIME_ZONE = 'America/New_York'

STATIC_URL = '/static/'

```

2. Add following entries

```
# Add at the begining of the file
import os

# Add following settings at the bottom of the file

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

ACCOUNT_EMAIL_VERIFICATION = 'none'

LOGIN_REDIRECT_URL = '/'

SOCIALACCOUNT_LOGIN_ON_GET = True
ACCOUNT_LOGOUT_ON_GET = False
SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email'
        ], 
        'AUTH_PARAMS': {
            'access_type':'offline',
        }
    }
}

```

Now move to next step
## Overview

Primary goal of `django-accelerator-digidrey` is to skip the boilerplate setup, jump right into development, and concentrate on building core features and functionalities.

If you are looking at this from your working app, you have perform this step. Go to the second step - **Setup OAuth**.

#### Key Features

- **Mobile-First User Interface:** Pre-configured responsive and visually appealing mobile-friendly User Interface.

- **Google OAuth-Based Social Login:** Pre-configured Django allauth social package to utitilize Google OAuth-based social login, allowing users to effortlessly sign in using their existing Google accounts.

- **About Me & Disclaimer Page:** Pre-configured `about us` and `disclaimer` page templates, easy to personalized. 

- **Contact Us Page:** Pre-configured `contact us` page, backed by database for visitor to leave feedback, inquiries, or questions. 


#### Get Started

* Create project

```
mkdir myproject
cd myproject
git clone https://github.com/vhpatel73/django-accelerator-digidrey.git .
```

* Create Virtual Environment
```
python -m venv venv
source venv/bin/activate
```

* Install packages
```
pip install --upgrade pip
pip install -r requirements.txt
```

* Setup database
```
python manage.py migrate
```

* Setup admin account
```
python manage.py createsuperuser
```

* Run Unit Testcase 
```
python ./manage.py test
```

* Start server
```
python manage.py runserver --insecure
```
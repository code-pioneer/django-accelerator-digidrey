# django-accelerator-digidrey

Primary goal of `django-accelerator-digidrey` is to skip the boilerplate setup, jump right into development, and concentrate on building core features and functionalities.

## Key Features

- **Mobile-First User Interface:** Pre-configured responsive and visually appealing mobile-friendly User Interface.

- **Google OAuth-Based Social Login:** Pre-configured Django allauth social package to utitilize Google OAuth-based social login, allowing users to effortlessly sign in using their existing Google accounts.

- **About Me & Disclaimer Page:** Pre-configured `about us` and `disclaimer` page templates, easy to personalized. 

- **Contact Us Page:** Pre-configured `contact us` page, backed by database for visitor to leave feedback, inquiries, or questions. 


## Get Started
1. Create project

```
mkdir myproject
cd myproject
git clone https://github.com/vhpatel73/django-accelerator-digidrey.git .
```

2. Create Virtual Environment
```
python -m venv venv
source venv/bin/activate
```

3. Install packages
```
pip install --upgrade pip
pip install -r requirements.txt
```

4. Setup database
```
python manage.py migrate
```

5. Setup admin account
```
python manage.py createsuperuser
```

6. Unit Test 
```
python ./manage.py test
```

7. Start server
```
python manage.py runserver --insecure
```
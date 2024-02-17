# Finishing Touch
The goal of this step is to complete the authentication setup from previous step, apply some finishing touch, and fireup webserver.

Download `ref-app-v1.x.y.zip`, move into root directory, and expand (allow overwrite).

```
unzip ref-app-v1.x.y
pip3 install -r requirements.txt
python3 manage.py makemigrations home
python3 manage.py migrate
python3 manage.py runserver
```

#### One last step (configuring Google login) ...

Visit `http://localhost:8000/admin`

- Select "Social applications > ADD SOCIAL APPLICATION"
- Set Provider: Google
- Set Provider ID: XXXXXXXXXXXX
- Set Name: XXXXXXXXXXXX
- Set Client Id: XXXXXXXXXXXX
- Set Secret key: XXXXXXXXXXXX
- Set Sites: <Add whatever showing up i.e. example.com>

## Summary

You should have **fully functional application** with following features built-in.

1. Default theme based on extended bootstrap theme
2. Pre-configured standard static webpages
    * Homepage
    * About Us
    * Disclaimer
3. Documentation section (markdown files presented as tabs within 'documentation' section)
4. Social authentication based on '[allauth](https://docs.allauth.org/en/latest/)' framework, pre-configured with google as identity provider
5. Authencation protected
    * Profile page
    * Contact Us page

** Have a fun **
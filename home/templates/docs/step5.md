## Setup Postgresql database (Optional)
The goal of this optional step is to switch default (sqlite) database and use 'postgres' database.


#### Create POSTGRESQL database on local workstation
* Database name: rag
* DB Schema: ragschema
* Database user: rag_admin
* Database pwd : pass***

```
CREATE DATABASE rag;

CREATE USER rag_admin WITH PASSWORD '******';

GRANT ALL PRIVILEGES ON DATABASE rag TO rag_admin;

\connect rag;

ALTER ROLE rag_admin SET client_encoding TO 'utf8';

ALTER ROLE rag_admin SET default_transaction_isolation TO 'read committed';

ALTER ROLE rag_admin SET timezone TO 'UTC';
```

#### Configure Django to use POSTGRESQL database
In settings.py file,
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'OPTIONS': {
                'options': '-c search_path=ragschema'
            },
        'NAME': 'rag', 
        'USER': 'rag_admin', 
        'PASSWORD': '******',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    }
}
```
Add `psycopg2-binary` module in `requirements.txt`

#### Install packages, setup database, start server and verify

```
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python3 manage.py runserver
```

After database switch, you will have to reconfigure social login. Just go to admin view and follow "Configure Django Administration" section of "Setup OAuth".

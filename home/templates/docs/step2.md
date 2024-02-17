## Create Primary App (i.e. Home)
The goal for this app is to serve default homepage and other standard functions like
- Homepage
- Contact Us (with ability for visitor to leave feedback)
- About Us
- Disclaimer

#### Create 'home' app and verify

```
python3 manage.py startapp home 
python manage.py migrate
python manage.py createsuperuser
python3 manage.py runserver
```

Webserver should be running without any problem (verify [http://localhost:8000/](http://localhost:8000/)). Result should be same as before.


#### Summary


You should have working django application with following folder structure.
```
 + my_project
   + home (dir)
   + main (dir)
   + venv (dir)
   - db.sqlite3 (file)
   - manage.py (file)
   - requirements.txt (file)

```

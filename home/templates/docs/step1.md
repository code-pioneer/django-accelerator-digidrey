## Getting Started

#### Create directory for your project
```
mkdir my_project
cd my_project
```

#### Create python virtual environment and install Django
```
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
python3 -m pip install Django
python3 -m django --version
pip freeze > requirements.txt
```

#### Create a project and verify

Project name: main
```
django-admin startproject main .
python3 manage.py runserver
```
Webserver should be running without any problem (verify [http://localhost:8000/](http://localhost:8000/))

#### Summary

You should have working django application with following folder structure.
```
 + my_project
   + main (dir)
   + venv (dir)
   - db.sqlite3 (file)
   - manage.py (file)
   - requirements.txt (file)

```
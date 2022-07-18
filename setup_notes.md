# Restaurant Recommender

## Getting started...
1. install python 3.10
2. set up directory
    C:\Users\vnguy\Documents\food_rec_app
3. set up virtual env
    python -m venv py310
4. start virtual env
    source py310\Scripts\activate
5. install django
    pip install django
6. start django app
    django-admin startproject food_rec
    cd food_rec
    python manage.py startapp app
    python manage.py runserver
7. visit http://127.0.0.1:8000/
8. migrate
    python manage.py makemigrations
    python manage.py migrate

9. setup admin user
    python manage.py createsuperuser
    password: food_rec_app
10. add 'apps.app.AppConfig' to INSTALLED_APPS list under settings.py

## Setting up PostgreSQL
1. install pgadmin4
    pip install pgadmin4
2. run pgadmin4
    pgadmin4
3. https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8
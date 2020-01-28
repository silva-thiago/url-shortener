# URL Shortener
URL shortening service developed by Thiago Silva. The user could access a list of URLs that had been shortened in the 
past after logging in to their Account. And the user can see more information in the link "URLs List"
for any shortened URL.

## Starting project

#### Create the database in MySQL
* create database db_shortener_url

#### Inside the root directory, create and activate your venv
* python3 -m venv venv
* source venv/bin/activate

#### Install project dependencies
* pip install -r requirements.txt

#### System administrator access
* python3 manage.py createsuperuser

#### Creating the database tables
* python3 manage.py migrate

#### Migrating changes to the database
* python3 manage.py makemigrations

#### Running the project
* python3 manage.py runserver

#### Useful commands for development
* django-admin startproject PROJECT_NAME .
* python3 manage.py startapp MODULE_NAME
* python3 manage.py collectstatic
* pip install django
* pip install mysqlclient

#### Saving development dependencies to a file
* pip freeze > requirements.txt
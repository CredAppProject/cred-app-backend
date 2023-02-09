## Generating Secret Key
1. For generating the secret key in django, run ```python script.py```

This will generate an __.env__ variable in the root directory with django secret key, add key ```DEBUG = ``` with True in Developement and False in Production.

## Configuring PostgreSQL for the application
1. Create new database ```CREATE DATABASE <database_name>;```
2. Create new user for the database ```CREATE USER <username> WITH PASSWORD '<password>';```
3. Grant Super Admin role to the created user ```ALTER USER <username> WITH SUPERUSER;```
4. Update the database values in .env variable.

## Structure of .env variable
```
SECRET_KEY = 'auto generated django secret key'
DEBUG = True|False 
NAME = "database_name" 
USER = "username"
PASSWORD = "password" 
HOST = "db_host"
PORT = "db_port"
```

## Running the Application
Before running the application, make sure that you have installed and configured the PostgreSQL and also the .env variable.

1. ```pip install -r requirements.txt```  
2. ```python manage.py runserver```

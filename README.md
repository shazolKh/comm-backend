## Ecommerce project
___
### To run the project locally-
___
````
1. Clone the repo
2. cd comm-backend
3. create virtual environment- python -m venv venv
4. activate the environment- venv\Scripts\activate
5. pip install -r requirements.txt
6. python manage.py makemigrations
7. python manage.py migrate
````
Then create `.env` file at the root directory and enter the following values-
````
DJANGO_ENV=dev
SECRET_KEY=enter_your_secret_key
````
If `DJANGO_ENV=production` then enter following values in `.env` file
````angular2html
DBNAME=database_name_goes_here
DBHOST=db_host_here
DBUSER=db_user
DBPASS=db_password
DBPORT=db_port
````
Then follow the commands below -
````angular2html
8. python manage.py createsuperuser
9. python manage.py runserver
````

To see the request/response of the APIs, Go to the url `docs/`
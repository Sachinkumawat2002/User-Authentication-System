Download the project from git
Open in Editor and install pipenv (It install all the library and packages which is used in project)
Then set the database in setting.py (In this project I have used postgresql)
Run command in terminal makemigrations (It make migration file based on the model changes)
Run command in terminal migrate (It save the model or changes in database)
To run the project we need to run command python manage.py runserver
To create superuser we need to run command python manage.py createsuperuser
we can open admin panel on browser "baseurl/admin/"
we can see all the api on browser "baseurl/user/"
We can create user form create-user api
To create token we need to use auth api
We can get all user from get-all-user(We need to add token) API
We can get user by id from get-user-by-id (We need to add token) API
We can get user by id from update-user (We need to add token) API
For all the token we need to add mod header or we can use thunder in vs code or we can test api in Postman
# I did not use Map API because here API was asking to enable billing.

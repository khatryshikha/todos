# todos


We have used MySQL db, the app has a simple home page



todos
===================
A simple CRUD app in Django
 
> **Note:**

> - The bee app is for homepage, and in future to extend that, user logins etc.
> - The todos app has all the current main code for adding/showing the created entries. 

#### <i class="icon-file"></i> Running locally

 - Clone the repo
   >`git clone {{repo .git link}}`
 - Create a virtualenv with name venv
   >`virtualenv venv`
   Activate it 
   >`source venv/bin/activate`
   and run `pip install -r requirements.txt`. If you choose other name modify the .gitignore accordingly.
 - Create local database `python manage.py migrate ` and `python manage.py makemigrations`
 - Run it `python manage.py runserver `

Contributor @khatryshikha and @Pratibha-Goyal

Possible errors and their solutions:-
Error in installing Mysql dependency in pip
`sudo apt-get install libmysqlclient-dev`

MySQL not found
Install my SQL [Install MySQL](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-14-04)

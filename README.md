# BlogSlog: A web app written in Python using flask
This is a very simple web application written in python using the web application framework Flask. It's a very simple blog app
that will accept user input through forms. Hopefully it will even have an authentication system.

## What is this app for?
I created this app in order for me to get accustomed to using Postgresql with Flask. All of the other Flask apps that I've written have
just used sqllite, which is great for creating simple apps that run locally, but isn't that great for production. Hopefully this will help
to improve my skills with Postgresql and Flask.

## I wish to install this app for some reason. How do I go about doing that?

Fork and clone, baby!
### Installing requirements:

You can install the requirements easily on a Linux system with the following commands:

```
~$ virtualenv myVirtualEnvironment
~$ source /path/to/myVirtualEnvironment/bin/activate
~$ pip install -r requirements.txt
```

### Setting up the database:
This app uses postgresql for the database. This can easily be changed in `config.py` if you so desire, but you'll lose the ability to deploy it to Heroku. You can read how to set up a Postgresql database [here](https://www.postgresql.org/docs/8.1/static/manage-ag-createdb.html).

### Configuring the app
For convenience, everything that needs to be configured is in `config.py`. There are several ways to configure the app.

#### Configuring the app using environment variables:
This is the default configuration for the app.
```python
import os

DB_USER = os.environ["POSTGRES_USER"]
DB_PASSWORD = os.environ["POSTGRES_PASSWORD"]
DB_LOCATION = "my/database/path" #usually localhost/dbname

DB_URI = "postgresql://" + DB_USER + ":" + DB_PASSWORD + "@" + DB_LOCATION
```

Please note that this does require you to have environment variables for your postgresql username and password.
#### Configuring the app without environment variables (not recommended):
This is not recommended if you plan on deploying the app for some reason.
```python
import os

DB_USER = "my_user_name"
DB_PASSWORD = "my_password"
DB_LOCATION = "my/database/path"

DB_URI = "postgresql://" + DB_USER + ":" + DB_PASSWORD + "@" + DB_LOCATION

```
Or if you wish to use SQLlite3:
```python
DB_URI = "sqlite3:///my_database_name.db"
```

## Running the app:
Once you've gotten everything all set up, open up your favorite terminal program and type

 `python blogapp.py`

 You should see a message similar to this:
 ```
* Running on http://127.0.0.1:3000/
* Restarting with stat
* Debugger is active!
* Debugger pin code: 123-456-789
 ```
 Congratulations! You've gotten the app to run properly! You now have a useless blog application written in flask. Congratulations!

 All you need to do now is visit `localhost:3000` in your favorite browser and you've got a wonderful blog.

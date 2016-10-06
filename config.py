import os

DB_USER = os.environ["POSTGRES_USER"]
DB_PASSWORD = os.environ["POSTGRES_PASSWORD"]
DB_LOCATION = "localhost/blogapp"
try:
    development = {
        "HOST":"127.0.0.1",
        "PORT" : 3000,
        "DEBUG": True,
        "DB_URI": "postgresql://" + DB_USER + ":" + DB_PASSWORD + "@" + DB_LOCATION
        }
    production = {
        "HOST":"0.0.0.0",
        "PORT": 8080,
        "DEBUG" : False,
        "DB_URI" : os.environ["DATABASE_URL"]
    }
except KeyError:
    print "warning: There isn't a DATABASE_URL environment variable. That's bad."

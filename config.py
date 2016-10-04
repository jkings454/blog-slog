import os

DB_USER = os.environ["POSTGRES_USER"]
DB_PASSWORD = os.environ["POSTGRES_PASSWORD"]
DB_LOCATION = "localhost/blogapp"

DB_URI = "postgresql://" + DB_USER + ":" + DB_PASSWORD + "@" + DB_LOCATION

development = {
    "HOST":"127.0.0.1",
    "PORT" : 3000,
    "DEBUG": True,
    "DB_URI": DB_URI
    }
production = {
    "HOST":"0.0.0.0",
    "PORT": 8080,
    "DEBUG" : False,
    "DB_URI" : os.environ["DATABASE_URL"]
}

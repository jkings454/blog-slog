import os

DB_USER = os.environ["POSTGRES_USER"]
DB_PASSWORD = os.environ["POSTGRES_PASSWORD"]
DB_LOCATION = "localhost/blogapp"

DB_URI = "postgresql://" + DB_USER + ":" + DB_PASSWORD + "@" + DB_LOCATION

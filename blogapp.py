from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Post

import config

engine = create_engine(config.DB_URI)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask("__name__")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=config.development["DEBUG"],
     host=config.development["HOST"],
     port=config.development["PORT"])

from flask import Flask, render_template, request, redirect, url_for
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

@app.route("/posts")
def posts():
    posts = session.query(Post).all()
    return render_template("posts.html", posts=posts)

@app.route("/posts/<int:post_id>")
def show_post(post_id):
    post = session.query(Post).filter_by(id=post_id).one()
    return render_template("show_post.html", post=post)

@app.route("/posts/new", methods = ["GET", "POST"])
def new_post():
    print request
    if request.method == "POST":
        newPost = Post(content=request.form['content'],
                    title=request.form['title'])
        session.add(newPost)
        session.commit()
        return redirect(url_for("posts"))
    else:
        return render_template("new_post.html")


if __name__ == "__main__":
    app.run(debug=config.production["DEBUG"],
     host=config.production["HOST"],
     port=config.production["PORT"])

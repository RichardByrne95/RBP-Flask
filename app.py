import os
from flask_pymongo import MongoClient
from flask import Flask, flash, render_template, redirect, url_for


app = Flask(__name__)

app.config["MONGO_DB_NAME"] = os.getenv("MONGO_DB_NAME")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.secret_key = os.getenv("SECRET_KEY")

mongo = MongoClient(os.getenv("MONGO_URI"))
db = mongo.get_database("RBP")


@app.route("/")
@app.route("/home")
def home():
    try:
        return render_template("index.html")

    except Exception as e:
        flash("Error loading page. ", f"Error: {e}")
        return render_template("404.html")


@app.route("/studios")
def studios():
    try:
        return render_template("studios.html",
                               page_wrapper_id="studios-wrapper")

    except Exception as e:
        flash("Error loading page. ", f"Error: {e}")
        return render_template("404.html")


@app.route("/artists")
def artists():
    try:
        return render_template("artists.html",
                               page_wrapper_id="artists-wrapper")

    except Exception as e:
        flash("Error loading page. ", f"Error: {e}")
        return render_template("404.html")


@app.route("/contact")
def contact():
    try:
        return render_template("contact.html",
                               page_wrapper_id="contact-wrapper")

    except Exception as e:
        flash("Error loading page. ", f"Error: {e}")
        return render_template("404.html")


@app.route("/blog")
def blog_home():
    blog_posts = list(db.blog_posts.find())
    return render_template("blog_home.html",
                           page_wrapper_id="blog-wrapper",
                           blog_posts=blog_posts)


@app.route("/insert_test_blog_post")
def insert_test_blog_post():
    test_blog_post = {
        "title": "Test Blog Post",
        "hero_image": "static/images/studioone/studio_one_3_amps.jpg",
        "author": "Richard Byrne",
        "url": "test-url"
    }
    try:
        db.blog_posts.insert_one(test_blog_post)

    except Exception as e:
        flash(f"Error: {e}")

    return redirect(url_for('home'))


@app.route("/blog/<blog_url>")
def blog_post(blog_url: str):
    blog_object = db.blog_posts.find_one({"url": blog_url})
    return render_template("blog_post_template.html", blog_post=blog_object)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEVELOPMENT"),
    )

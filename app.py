import os
from flask_pymongo import MongoClient
from flask import Flask, flash, render_template


app = Flask(__name__)

app.config["MONGO_DB_NAME"] = os.getenv("MONGO_DB_NAME")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.secret_key = os.getenv("SECRET_KEY")

mongo = MongoClient(os.getenv("MONGO_URI"))
db = mongo.get_database("ServerlessInstanceRBP")


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
    try:
        return render_template("blog.html",
                               page_wrapper_id="blog-wrapper")

    except Exception as e:
        flash("Error loading page. ", f"Error: {e}")
        return render_template("404.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEVELOPMENT"),
    )

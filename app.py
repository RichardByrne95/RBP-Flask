import os
from flask import Flask, flash, render_template, redirect, request, session, url_for


app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY")


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
                               page_wrapper_id="studios")

    except Exception as e:
        flash("Error loading page. ", f"Error: {e}")
        return render_template("404.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEVELOPMENT"),
    )

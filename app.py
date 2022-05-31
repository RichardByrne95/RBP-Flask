import os
from flask import Flask, flash, render_template, redirect, request, session, url_for


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    """Homepage"""
    try:
        return render_template("index.html")

    except Exception as e:
        flash("Error loading page. ", f"Error: {e}")
        return render_template("404.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEVELOPMENT"),
    )

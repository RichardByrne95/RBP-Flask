import os
from flask import Flask, flash, render_template, redirect, request, session, url_for


app = Flask(__name__)


@app.route("/")
def index():
    """Homepage"""
    return "Hello world"


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEVELOPMENT"),
    )

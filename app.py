import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def index():
    return render_template("login.html")


@app.route("/profile")
def index():
    return render_template("profile.html")


@app.route("/search")
def index():
    return render_template("search.html")


if __name__ = "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug == True)

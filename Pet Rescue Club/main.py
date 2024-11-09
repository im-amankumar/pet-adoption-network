from flask import Flask
from flask import redirect
from flask import url_for, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.before_request("/")
def before_request():
    return render_template("contract.py")


if __name__=="__main__":
    app.run()
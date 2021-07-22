from flask import Flask, flash, redirect, render_template, request, session, abort
from bokeh.embed import server_document

app = Flask(__name__)

"""@app.route('/')
def home():
    return render_template("home.html")"""

@app.route("/")
def home():
    script=server_document("home.html")
    return render_template('home.html',bokS=script)


@app.route("/about/")
def about():
    script=server_document("about.html")
    return render_template('about.html',bokS=script)

if __name__== "__main__":
    app.run()

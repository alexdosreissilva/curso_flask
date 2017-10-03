from flask import render_template
from app import app


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/post/<int:id>")
def post(id):
    return "Post: %d" % id

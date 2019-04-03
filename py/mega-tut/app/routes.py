from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def hello():
  return "hello, world!"

@app.route("/test")
def test():
  return render_template("test.html", 
  title=None,
  items=["abc", "def"],
  user={'username': 'Dinesh'})
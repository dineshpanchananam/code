from flask import (
  Flask,
  jsonify,
  request,
  session,
  make_response
)
from time import sleep
from random import randint

app = Flask(__name__)

@app.route('/')
def home():
  sleep(0.04)
  return "hello, world!"

@app.route("/vote/<int:age>")
def can_vote(age):
  if not 1 <= age <= 130:
    response = make_response(jsonify({'errors': 'Enter a valid age'}), 400)
    return response
  return jsonify({'canVote': age >= 18})

@app.route("/bad")
def bad_request():
  response = make_response("nope, can't do it", 400)
  response.headers['X-abc'] = '3'
  return response

@app.route("/post", methods=["POST"])
def post_only():
  return '{}'

@app.route('/test/<doc_id>/ann', methods=["PUT"])
def put_endp(doc_id):
  return "yay!"

if __name__ == '__main__':
  app.run()
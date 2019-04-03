from flask import Flask, jsonify, request, make_response
from flask import session
import requests as r

app = Flask(__name__)
app.secret_key = 'terces'

@app.route("/")
def home():
  return jsonify(dict(request.headers.items()))

@app.route("/cookies")
def cookies():
  return jsonify({
    'cookies': request.cookies,
    'keys': request.cookies.keys()
  })

@app.route("/jsonify")
def home2():
  res = jsonify({'cookie': 'set'})
  res = make_response(res)
  res.set_cookie('foo', 'bar')
  return res

@app.route('/crookie')
def cmp_cook():
  res = make_response('OK')
  res.set_cookie('foo', 'bax', max_age=0)
  return res

@app.route("/visit")
def home4():
  if 'visits' not in session:
    session['visits'] = 0
  session['visits'] += 1
  return jsonify({
    'visits': session['visits'],
  })

@app.route("/pop")
def home5():
  session['pops'] = session.get('pops', 0) + 1
  # session.pop('visits', None)
  return jsonify(dict(session.items()))

app.run(
  debug=True,
  port=7999+1
)
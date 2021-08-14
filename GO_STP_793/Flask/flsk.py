#!/usr/bin/env python
from flask import Flask
from flask import render_template
from flask import redirect, url_for
from flask import *


app = Flask(__name__)

#which url to access
@app.route('/')   #goes to the homepage
def home():
    return render_template('index.html')

@app.route("/courses")
def courses():
    return "<h1>Courses</h1>"

@app.route("/<name>")
def user(name):
	return f"<h1> hello {name}"
	
@app.route('/results/<int:marks>')    
def results(marks):
    return redirect(url_for('success', marks = marks))


@app.route('/success/<int:marks>')
def success(marks):
    final = ""
    if marks <45:
        final = 'Fail'
    else:
        final = 'pass'

    result = {'number':marks, 'result':final}
    return render_template('result.html', result = result)
#images go in static named folder
#html files to be rendered can go in templates folder

@app.route("/about")
def about():
	return render_template('about.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    marks = 0
    if request.method == 'POST':
        phy = request.form['physics']
        chem = request.form['Chemistry']
        math = request.form['Maths']
        total = (phy+chem+math)/3
    marks = total
    return redirect(url_for('success', marks = marks))

'''
get is to send data to the server unencrypted

post - send form data, it is never cached, it is  encrypted
'''

'''
jinja 2 template delimiter

{{   }}   -  for any kind of expressions or simply some variable
{%    %}  -  for  statements
{#    #}  -  for comments

'''


if __name__ == '__main__':
    app.run(debug = True)


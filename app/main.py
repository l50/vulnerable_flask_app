#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, abort, flash, make_response, redirect, render_template, request, session, url_for
import base64
import os
import subprocess

__auth__ = 'jayson.e.grace@gmail.com'


app = Flask(__name__)
app.secret_key = os.urandom(12)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return redirect(url_for("hello"))


@app.route('/hello/', methods=['GET'])
def hello():
	if request.args.get('name'):
		f = """
	    <html>
	    <h1>Hello """ + request.args.get('name') + """</h1>
	    </html>
	    """
		return f
	else:
		f = """
		<html>
	    <h1>Please input your name in the name parameter, i.e. http://localhost:5000/hello?name=bob</h1>
	    </html>
	    """
		return f


@app.route('/login', methods=['POST'])
def login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        response = redirect(url_for("home"))
        response.set_cookie('YourSessionCookie', 'admin')
        session['logged_in'] = True
        return response
    else:
        return redirect(url_for('home'))


@app.route('/command_runner')
def command_runner():
    if request.args.get('cmd'):
        cmd = [request.args.get('cmd')]
        try:
            out = subprocess.check_output(cmd, shell=True)
        except subprocess.CalledProcessError as e:
            return f"Unable to run {cmd}."

        return out


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)

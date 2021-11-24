from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, make_response
from flask import render_template
from wtforms import Form, StringField, TextAreaField, PasswordField, validators


app = Flask(__name__)
app.template_folder = 'templates'

@app.route("/")
def index():
    return Flask.redirect('/login')

@app.route("/login")
def login():
    return render_template("login.html")

class RegisterForm(Form):
	nickname = StringField('Nickname', [validators.Length(min=1, max=50)])
	email = StringField('Email', [validators.Length(min=6, max=50)])
	password = PasswordField('Password', [
		validators.DataRequired(),
		validators.EqualTo('confirm', message='Passwords do not match')
	])
	confirm = PasswordField('Confirm Password')

@app.route("/registrar")
def registrar():
    form = RegisterForm(request.form)
    return render_template("registrar.html", form=form)

# run
app.run(host='127.0.0.1', port=8000, debug=True)
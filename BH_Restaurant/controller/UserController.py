from app import app
from flask import Flask, render_template



@app.route('/user_registration')
def register():
    return render_template('user_registration.html')

@app.route('/registration', methods=['GET','POST'])
def userRegister():
    return 'ok'

@app.route('/login')
def login():
    return render_template('login.html')
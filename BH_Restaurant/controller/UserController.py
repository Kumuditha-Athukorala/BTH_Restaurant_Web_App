from flask import *
from app import app
from service.UserService import UserService

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/checklogin', methods=['POST'])
def checkUserLogin():
    session.pop('user', None)
    postData = request.form
    print(postData)

    userService = UserService()
    result = userService.checkUserLogin(postData)
    print(result)

    return str(result)

@app.route('/profile')
def profile():
    if session.get("user") is None:
        return render_template('login.html')
    else:
        return render_template('profile.html')

@app.route('/logout')
def logout():
    session.pop('user',None)
    return render_template('index.html')

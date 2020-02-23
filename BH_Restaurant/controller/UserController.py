
from flask import *
from app import app
from service.UserService import UserService

@app.route('/customer_registration')
def register():
    return render_template('customer_registration.html')

@app.route('/registration', methods=['GET','POST'])
def userRegister():
    return 'ok'

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/checklogin', methods=['POST'])
def checkUserLogin():

    postData = request.form
    print(postData)

    userService = UserService()
    result = userService.checkUserLogin(postData)
    print(result)

    return str(result)















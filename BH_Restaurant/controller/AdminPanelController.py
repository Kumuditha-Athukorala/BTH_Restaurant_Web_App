from flask import *
from app import app
from service.UserService import UserService

userService = UserService()

@app.route('/adminpanel')
def adminPanel():
    if(session['user'] == 'Kuma'):
        return render_template('admin_panel.html')
    else:
        return render_template('index.html')

@app.route('/viewallcustomers', methods=['POST'])
def viewAllCustomers():
    resultAllCustomers = userService.allCustomers()
    print(resultAllCustomers)
    print(type(resultAllCustomers))


    return "1"
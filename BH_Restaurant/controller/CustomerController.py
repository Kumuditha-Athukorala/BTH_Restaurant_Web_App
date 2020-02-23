from flask import *
from app import app
from service.CustomerService import CustomerService

customerService = CustomerService()


@app.route('/customer_registration',methods=['GET'])
def register():
    return render_template('customer_registration.html')

@app.route('/register',methods=['POST'])
def registerCustomer():
    print('customer')
    postData = request.form
    print(postData)

    result = customerService.checkCustomerEmail(postData)
    print(result)

    return str(result)
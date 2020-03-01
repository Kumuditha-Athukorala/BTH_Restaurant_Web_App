from flask import *
from app import app
from service.CustomerService import CustomerService
from service.UserService import UserService
from service.TableBookingService import TableBookingService
from service.EmailService import EmailBTH



import json

userService = UserService()
bookingService = TableBookingService()
customerService = CustomerService()

emailbth = EmailBTH()

@app.route('/adminpanel')
def adminPanel():
    if(session['user'] == 'Kuma'):
        return render_template('admin_panel.html')
    else:
        return render_template('index.html')

@app.route('/viewallcustomers', methods=['POST'])
def viewAllCustomers():

    resultAllCustomers = userService.allCustomers()
    customer_json_string = json.dumps(resultAllCustomers)

    session["allusers"] = resultAllCustomers

    return customer_json_string

@app.route('/viewallbookings', methods=['POST'])
def viewAllBookings():

    resultAllBookings = bookingService.getAllBookings()
   # booking_json_string = json.dumps(resultAllBookings)

    session["allbookings"] = resultAllBookings
    print(resultAllBookings)

    return "1"

@app.route('/changecustomerstatus', methods=['POST'])
def changeCustomerStatus():

    postData = request.form
    print(postData)

    result = customerService.updateUserStatus(postData)
    print(result)

    return "1"


@app.route('/cancel_or_process_order', methods=['POST'])
def cancelOrder():

    print("cancel_or_process_order")
    postData = request.form
    print(postData)
    purpose = postData.get("o_purpose")
    print(purpose)

    id = postData.get("o_id")
    print(id)

    result = emailbth.sendEmail(postData)
    print(result)
    bookingService.processBookingOrder(result,id)

    return "1"


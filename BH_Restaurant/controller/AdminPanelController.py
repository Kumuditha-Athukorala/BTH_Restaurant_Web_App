from flask import *
from app import app
from service.UserService import UserService
from service.TableBookingService import TableBookingService
import json

userService = UserService()
bookingService = TableBookingService()

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



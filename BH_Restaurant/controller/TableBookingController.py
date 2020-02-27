from flask import *
from app import app
from service.TableBookingService import TableBookingService

tableBookingService = TableBookingService()

@app.route('/booktable')
def tableBooking():
    if session.get("user") is None:
        return render_template('login.html')
    else:
        return render_template('table_booking.html')


@app.route('/booking',methods=['POST'])
def booking():
    print('booking')
    postData = request.form
    print(postData)

    result = tableBookingService.saveTableBookingRecord(postData)
    print(result)

    return str(result)
from flask import *
from app import app


@app.route('/booktable')
def tableBooking():
    return render_template('table_booking.html')


@app.route('/booking',methods=['POST'])
def booking():
    print('register')
    postData = request.form
    print(postData)

    return '1'
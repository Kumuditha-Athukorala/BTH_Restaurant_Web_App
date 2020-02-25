from flask import *
from app import app


@app.route('/booktable')
def booking():
    return render_template('table_booking.html')
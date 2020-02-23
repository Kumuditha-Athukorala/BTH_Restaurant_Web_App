from flask import *
from app import app



@app.route('/customer_registration')
def register():
    return render_template('customer_registration.html')

@app.route('/register')
def registerCustomer():
    return 'ok';
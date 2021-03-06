from flask import *
from app import app
from service.CustomerService import CustomerService
from service.UserService import UserService
from service.TableBookingService import TableBookingService
from service.CategoryService import CategoryService
from service.EmailService import EmailBTH

ALLOWED_EXTENSIONS = {'jpg', 'jpeg','png'}


import json
import base64

userService = UserService()
bookingService = TableBookingService()
customerService = CustomerService()
catService = CategoryService()

emailbth = EmailBTH()

@app.route('/adminpanel')
def adminPanel():
    if(session.get("email") is not None and session['user_type'] == 'Admin'):

        resultAllCustomers = viewAllCustomers()
        resultAllBookings = viewAllBookings()
        return render_template('admin_panel.html',custData=resultAllCustomers, bookingData= resultAllBookings)
    else:
        return render_template('index.html')


def viewAllCustomers():

    resultAllCustomers = userService.allCustomers()
    # customer_json_string = json.dumps(resultAllCustomers)

    session["allusers"] = resultAllCustomers

    return resultAllCustomers


def viewAllBookings():

    resultAllBookings = bookingService.getAllBookings()
    #booking_json_string = json.dumps(resultAllBookings)

    session["allbookings"] = resultAllBookings
    print(resultAllBookings)

    return resultAllBookings

@app.route('/changecustomerstatus', methods=['POST'])
def changeCustomerStatus():

    if (session.get("email") is not None and session['user_type'] == 'Admin'):
        postData = request.form
        print(postData)

        result = customerService.updateUserStatus(postData)
        print(result)

        return "1"

    else:
        return render_template('index.html')



@app.route('/cancel_or_process_order', methods=['POST'])
def cancelOrder():

    if (session.get("email") is not None and session['user_type'] == 'Admin'):
        print("cancel_or_process_order")
        postData = request.form
        print(postData)
        purpose = postData.get("o_purpose")
        print(purpose)

        id = postData.get("o_id")
        print(id)

        result = emailbth.sendEmail(postData)
        print(result)
        bookingService.processBookingOrder(result, id)

        return "1"
    else:
        return render_template('index.html')





@app.route('/addNewCategory', methods=['POST'])
def newCategory():
    if (session.get("email") is not None and session['user_type'] == 'Admin'):
        print("cateeeee")
        postData = request.form
        print(postData)

        result = catService.saveFoodCategory(postData)
        print(result)
        return str(result)
    else:
        return render_template('index.html')


@app.route('/addMenu', methods=['POST', 'GET'])
def addMenuItem():
    if (session.get("email") is not None and session['user_type'] == 'Admin'):

        print("Menu Item")
        postData = request.form
        img_file = request.files['file']
        encr_img = base64.b64encode(img_file.read())

        if 'file' not in request.files:
            flash('No File Part in Request')
            return redirect(url_for('adminPanel'))

        if img_file.filename == '':
            flash('There is no selected Image')
            return redirect(url_for('adminPanel'))

        if img_file and checkFileExtension(img_file.filename):
            catService.saveMenuItem(postData, encr_img)
            flash('Menu Item Added Successfully...!')
            return redirect(url_for('adminPanel'))
        else:
            flash('Wrong File Selection...!')
            return redirect(url_for('adminPanel'))


def checkFileExtension(fileName):
    print("extension")
    return '.' in fileName and \
           fileName.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/allCategories',methods=['POST'])
def allCategories():
    if (session.get("email") is not None and session['user_type'] == 'Admin'):
        resultSet = catService.getAllCtegories()
        session['Categories'] = resultSet
        print(resultSet)
        return "None"
    else:
        return render_template('index.html')






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
    if(session['email'] == 'kumudithaudesha@gmail.com'):
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

@app.route('/addNewCategory', methods=['POST'])
def newCategory():
    print("cateeeee")
    postData = request.form
    print(postData)

    result = catService.saveFoodCategory(postData)
    print(result)
    return str(result)

# @app.route('/addMenuItem', methods=['POST'])
# def addMenu():
#     print("adddddd")
#
#     postData = request.form
#     print(postData)
#
#     # result = catService.saveMenuItem(postData)
#     # print(result)
#
#     return "1"

@app.route('/addMenu',methods=['POST','GET'])
def addMenuItem():

    print("Menu Item")
    postData = request.form
    img_file = request.files['file']
    encr_img = base64.b64encode(img_file.read())

    if 'file' not in request.files:
        flash('No File Part in Request')
        return redirect(request.url)


    if img_file.filename == '':
        flash('There is no selected Image')
        return redirect(request.url)

    if img_file and checkFileExtension(img_file.filename):
        catService.saveMenuItem(postData,encr_img)
        return render_template('admin_panel.html')
    else:
        flash('Wrong File Selection...!')
        return redirect((request.url))

def checkFileExtension(fileName):
    print("extension")
    return '.' in fileName and \
           fileName.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/allCategories',methods=['POST'])
def allCategories():

    resultSet = catService.getAllCtegories()
    session['Categories'] = resultSet
    print(resultSet)
    return "None"




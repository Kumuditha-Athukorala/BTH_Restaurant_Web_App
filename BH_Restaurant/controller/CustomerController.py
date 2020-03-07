from flask import *
import base64
from app import app
from service.CustomerService import CustomerService
from service.CategoryService import CategoryService
from dao.BTMenu import BTMenu

customerService = CustomerService()
catService = CategoryService()


@app.route('/customer_registration',methods=['GET'])
def register():
    return render_template('customer_registration.html')

@app.route('/checkEmail',methods=['POST'])
def checkEmail():
    print('customer')
    postData = request.form
    print(postData)

    result = customerService.checkCustomerEmail(postData)
    print(result)

    return str(result)

@app.route('/registerCustomer',methods=['POST'])
def registerCustomer():

    print('register')
    postData = request.form
    print(postData)

    result = customerService.rgisterCustomer(postData)
    print(result)

    return str(result)

@app.route('/updateCustomer', methods=['POST'])
def updateCustomerDetails():
    print("Update")

    postData = request.form
    print(postData)

    userId = session.get("userId")
    result = customerService.updateCustomerDetails(postData,userId)

    print(result)
    return str(result)


@app.route('/ourMenu', methods=['GET'])
def ourMenu():
    print("Menu")
    MainCategories = catService.getAllCtegories()
    MenuItems = catService.getMenuItemsWithCategory()
    print(type(MenuItems))
    Items=[]
    for i in MenuItems:
        btm = BTMenu(i['menu_id'],i['menu_name'],i['price'], i['image'].decode("UTF-8"),i['description'],i['status'],i['category_id'],i['cat_name'])
        Items.append(btm)

    print(Items)

    print(type(MainCategories))
    print(type(MenuItems))

    return render_template('Menu.html',data=MainCategories, Item_List = Items)


@app.route('/forgotemail', methods=['POST'])
def forgotPassword():
    print("forgettttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt")

    emData =request.form
    print(emData)

    result = customerService.recoverPassword(emData)
    print("fgggggggggggggggggggggggggggggggggggggggggggggggggggggggtttttttttttt")
    print(result)

    return result

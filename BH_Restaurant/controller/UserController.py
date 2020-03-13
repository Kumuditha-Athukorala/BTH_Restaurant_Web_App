from flask import *
from app import app
from service.UserService import UserService
from service.TableBookingService import TableBookingService

userService = UserService()
bookingService = TableBookingService()

@app.route('/login', methods=['GET','POST'])
def login():
    if session.get("email") is None:
        return render_template('login.html')
    else:
        return render_template('index.html')


@app.route('/checklogin', methods=['POST','GET'])
def checkUserLogin():
    if request.method == 'POST':
        session.pop('user_type', None)
        session.pop('user', None)
        session.pop('userId', None)
        session.pop('email', None)
        postData = request.form
        print(postData)

        result = userService.checkUserLogin(postData)
        print(result)

        return str(result)
    else:
        return render_template('index.html')


@app.route('/profile',methods=['POST','GET'])
def profile():
    if session.get("email") is None:
        return render_template('login.html')
    else:
        myBookings = getMyBookings()
        return render_template('profile.html', bookingList = myBookings)

@app.route('/logout')
def logout():
    session.pop('user_type', None)
    session.pop('user', None)
    session.pop('userId', None)
    session.pop('email', None)

    return render_template('index.html')


def getMyBookings():
    if session.get("email") is None:
        return render_template('login.html')
    else:
        userId = session.get("userId")
        print(userId)
        print(type(userId))
        resultSet = bookingService.getMyBookingDetails(userId)

        session["MyBookings"] = resultSet
        print(resultSet)

        return resultSet

@app.route('/changePassword', methods=['POST','GET'])
def changePassword():
    if session.get("email") is None:
        return render_template('login.html')
    else:
        userId = session.get("userId")
        print(userId)

        postData = request.form
        print(postData)

        result = userService.changePassword(postData,userId)

        print("change password")
        print(result)

        return "1"

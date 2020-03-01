from flask import *
from app import app
from service.UserService import UserService
from service.TableBookingService import TableBookingService

userService = UserService()
bookingService = TableBookingService()

@app.route('/login', methods=['GET','POST'])
def login():
    if session.get("user") is None:
        return render_template('login.html')
    else:
        return render_template('index.html')


@app.route('/checklogin', methods=['POST'])
def checkUserLogin():
    session.pop('user', None)
    postData = request.form
    print(postData)

    result = userService.checkUserLogin(postData)
    print(result)

    return str(result)

@app.route('/profile')
def profile():
    if session.get("user") is None:
        return render_template('login.html')
    else:
        return render_template('profile.html')

@app.route('/logout')
def logout():
    session.pop('user',None)
    return render_template('index.html')


@app.route('/mybookings', methods=['POST'])
def getMyBookings():
    if session.get("user") is None:
        return render_template('login.html')
    else:
        userId = session.get("userId")
        print(userId)
        print(type(userId))
        resultSet = bookingService.getMyBookingDetails(userId)

        session["MyBookings"] = resultSet
        print(resultSet)

        return "1"

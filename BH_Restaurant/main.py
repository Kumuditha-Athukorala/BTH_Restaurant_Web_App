from app import app
from flask import Flask, render_template,session
from controller import UserController,CustomerController,TableBookingController



@app.route('/')
def index():
    print(session.get("user"))
    return render_template('index.html',)


if __name__ == '__main__':
	app.run(debug=True)
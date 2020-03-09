from app import app
from flask import Flask, render_template,session
from controller import UserController,CustomerController,TableBookingController,AdminPanelController



@app.route('/')
def index():
    print(session.get("user"))
    return render_template('index.html',)

@app.errorhandler(404)
def error404(error):
    return '<h1>Custom Error Page for 404</h1>',404



if __name__ == '__main__':
	app.run(debug=True)
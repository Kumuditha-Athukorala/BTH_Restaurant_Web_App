from app import app
from flask import Flask, render_template,session
from controller import UserController,CustomerController,TableBookingController,AdminPanelController



@app.route('/')
def index():
    
    print(session.get("user"))
    return render_template('index.html',)

@app.errorhandler(404)
def error404(error):
    return render_template('404Page.html')

@app.errorhandler(500)
def error500(error):
    return render_template('500Page.html')

@app.errorhandler(405)
def error405(error):
    return render_template('405Page.html')


if __name__ == '__main__':
	app.run(debug=True)
from flask import Flask, render_template
from database import Database
app = Flask(__name__)

@app.route('/')
def index():

    db = Database()
    cursor = db.getDatabaseConnection()
    cursor.execute("Select * from customer")
    fetchdata = cursor.fetchall()
    return render_template('index.html', data = fetchdata)

@app.route('/user_registration')
def register():
    return render_template('user_registration.html')

@app.route('/registration', methods=['GET','POST'])
def userRegister():
    return 'ok'

@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
	app.run()
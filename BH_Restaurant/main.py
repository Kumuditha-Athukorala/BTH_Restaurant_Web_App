from app import app
from flask import Flask, render_template
from controller import UserController


@app.route('/')
def index():
    return render_template('index.html',)


if __name__ == '__main__':
	app.run()
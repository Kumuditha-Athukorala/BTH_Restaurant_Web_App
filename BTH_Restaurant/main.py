from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/slider')
def indexslider():
    return render_template('imageslider.html')

if __name__ == '__main__':
	app.run()
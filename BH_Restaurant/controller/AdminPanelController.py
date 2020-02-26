from flask import *
from app import app



@app.route('/adminpanel')
def adminPanel():
    if(session['user'] == 'Kuma'):
        return render_template('admin_panel.html')
    else:
        return render_template('index.html')
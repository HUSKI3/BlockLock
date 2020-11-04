from flask import render_template, jsonify
from app import app
import random
from NeblApi import *
import json, re
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/map')
def map():
    return render_template('map.html', title='Map')

"""
Create a form
[Send] - button
"""

class SendForm(Form):
    starting = SubmitField(label='Starting')
    ending = SubmitField(label='Ending')

@app.route('/apilogin/<addr>', methods=['GET', 'POST'])
def apilogin(addr):
    form = SendForm()
    if form.validate_on_submit():
        out = test_transaction()
        return str(out)
    if addr == "web":
        bal = get_balance(website=True)
    else:
        bal = get_balance(address=addr)
    # Use this awful thing to convert it into a valid format
    bal  = re.sub(r"[\n\t\s]*", "", str(bal).replace("\'", "\"").replace("None", '"None"'))
    data = json.loads(bal)
    return render_template('apilogin.html', title='Nebl API Login', bal=data['balance'],sent=data['total_sent'],rec=data['total_received'],tran=data['transactions'])

@app.route('/map/refresh', methods=['POST'])
def map_refresh():
    points = [(random.uniform(48.8434100, 48.8634100),
               random.uniform(2.3388000, 2.3588000))
              for _ in range(random.randint(2, 9))]
    return jsonify({'points': points})


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

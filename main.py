import json
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

with open('config.json', 'r') as c:
    params = json.load(c)['params']

app =Flask(__name__,template_folder='templates')
# app.secret_key = 'super-secret-key'
local_server = True

if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
    
db = SQLAlchemy(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

app.run(debug=True)
import json
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"



@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

app.run(debug=True)
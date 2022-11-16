# from application import db 


# db.create_all()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/expense'
db = SQLAlchemy(app)
Bootstrap(app)


with app.app_context():
    db.create_all()

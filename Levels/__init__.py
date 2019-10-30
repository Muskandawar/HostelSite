import os
from flask import Flask
from flask_pymongo import PyMongo
from flask_login import LoginManager
from flask_mail import Mail, Message


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
lm = LoginManager()
lm.init_app(app)

app.config["SECRET_KEY"] = "MYSECRETKEY"

##############################################

app.config["MONGO_URI"] = "mongodb://localhost:27017/HOSTELMANAGEMENT"
mongo = PyMongo(app)
users_db = mongo.db.USERDETAILS
complaints_db = mongo.db.COMPLAINTDETAILS
caretaker_db = mongo.db.CARETAKERLOGIN
admin_db = mongo.db.ADMINLOGIN

##############################################
app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'dawarmuskan21@gmail.com',
	MAIL_PASSWORD = 'patience@21'
	)
mail = Mail(app)

#############################################

from Levels import views

from Levels.admin.views import admin_blueprint
from Levels.caretaker.views import caretaker_blueprint
from Levels.user.views import user_blueprint

app.register_blueprint(admin_blueprint,url_prefix = '/admin')
app.register_blueprint(caretaker_blueprint,url_prefix = '/caretaker')
app.register_blueprint(user_blueprint,url_prefix = '/user')


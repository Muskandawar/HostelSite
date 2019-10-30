from flask import (Blueprint, flash, redirect, render_template, request,
                   session, url_for)
from flask_login import login_required, login_user, logout_user

from Levels import app, lm,mongo,caretaker_db
from Levels.forms import LoginForm, Registration
from Levels.authenticate_model import Authenticate
from werkzeug.security import generate_password_hash, check_password_hash

caretaker_blueprint = Blueprint('caretaker',__name__, template_folder='templates', static_folder='static')

@caretaker_blueprint.route('/',methods=['GET', 'POST'])
def caretaker_login():
    email = session.get('email',None)
    password = session.get('password',None)
    caretaker = caretaker_db.find_one({"email": email})
    if caretaker and Authenticate.validate_login(caretaker['password'], password):
        caretaker_obj = Authenticate(caretaker['email'])
        login_user(caretaker_obj) 
        flash("Logged in successfully!")    
        return redirect(request.args.get("next") or url_for("caretaker.caretaker_details"))
    flash("Wrong username or password!")
    return redirect(url_for('index'))

@caretaker_blueprint.route('/logout',methods=['GET', 'POST'])
def logout():
    logout_user()
    flash("Logged out successfully!")
    return redirect(url_for('index'))

@caretaker_blueprint.route('/caretaker_details',methods=['GET', 'POST'])
@login_required
def caretaker_details(): 
    return render_template('caretaker/index.html')

@lm.user_loader
def load_user(email):

    caretaker = caretaker_db.find_one({"email": email})
    if not caretaker:
        return None
    return Authenticate(caretaker['email'])


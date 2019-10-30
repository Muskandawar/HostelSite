from flask import (Blueprint, flash, redirect, render_template, request,
                   session, url_for)
from flask_login import login_required, login_user, logout_user

from Levels import app, lm,mongo,admin_db
from Levels.forms import LoginForm, Registration
from Levels.authenticate_model import Authenticate
from werkzeug.security import generate_password_hash, check_password_hash

admin_blueprint = Blueprint('admin',__name__, template_folder='templates', static_folder='static')

@admin_blueprint.route('/',methods=['GET', 'POST'])
def admin_login():
    email = session.get('email',None)
    password = session.get('password',None)
    admin = admin_db.find_one({"email": email})
    if admin and Authenticate.validate_login(admin['password'], password):
        admin_obj = Authenticate(admin['email'])
        login_user(admin_obj) 
        flash("Logged in successfully!")    
        return redirect(request.args.get("next") or url_for("admin.admin_details"))
    flash("Wrong username or password!")
    return redirect(url_for('index'))

@admin_blueprint.route('/logout',methods=['GET', 'POST'])
def logout():
    logout_user()
    flash("Logged out successfully!")
    return redirect(url_for('index'))

@admin_blueprint.route('/admin_details',methods=['GET', 'POST'])
@login_required
def admin_details(): 
    return render_template('admin/index.html')

@lm.user_loader
def load_user(email):

    admin = admin_db.find_one({"email": email})
    if not admin:
        return None
    return Authenticate(admin['email'])
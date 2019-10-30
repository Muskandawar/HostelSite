from flask import (Blueprint, flash, redirect, render_template, request,
                   session, url_for)
from flask_login import login_required, login_user, logout_user
from flask_mail import Mail, Message

from Levels import app, lm, users_db,mail,complaints_db,mongo
from Levels.forms import LoginForm, Registration,ComplaintForm
from Levels.authenticate_model import Authenticate
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import random as r

user_blueprint = Blueprint('user',__name__, template_folder='templates', static_folder='static')

@user_blueprint.route('/',methods=['GET', 'POST'])
def user_login():
    email = session.get('email',None)
    password = session.get('password',None)
    user = users_db.find_one({"email": email})
    if user and Authenticate.validate_login(user['password'], password):
        user_obj = Authenticate(user['email'])
        login_user(user_obj) 
        flash("Logged in successfully!")    
        return redirect(request.args.get("next") or url_for("user.user_details"))
    flash("Wrong username or password!")
    return redirect(url_for('index'))

@user_blueprint.route('/logout',methods=['GET', 'POST'])
def logout():
    logout_user()
    flash("Logged out successfully!")
    return redirect(url_for('index'))

@user_blueprint.route('/user_details',methods=['GET', 'POST'])
@login_required
def user_details(): 
    email = session.get('email', None)  
    user = users_db.find_one({"email": email})
    form = ComplaintForm()
    if form.validate_on_submit(): 
        session['complaint_type'] = form.complaint_type.data
        session['subject'] = form.subject.data
        session['complaint_desc'] = form.complaint_desc.data
        complaints_db.insert_one(
                    {
                        'rollno' : user['rollno'] , 'complaint_type' : session['complaint_type'] , 'subject' : session['subject'],
                        'complaint_desc' : session['complaint_desc'], 'comments' : None, 'caretaker_id' : None, 'assignee' : None, 'expected_date' : None, 'status_info' : {'status' : 1 , "timestamp" : [datetime.timestamp(datetime.now())]}
                    }
                )
    return render_template('user/index_user.html',email=email,form=form)

@lm.user_loader
def load_user(email):

    user = users_db.find_one({"email": email})
    if not user:
        return None
    return Authenticate(user['email'])


def register():
        hashpass = generate_password_hash(session['password'])
        users_db.insert_one(
            {
                "email" : str.lower(session['email']),"rollno" : session['rollno'], "hostel" : session['hostel'],
                "roomno" : session['roomno'] , "password": hashpass,"contact" : session['contact'],"complaints" : []
            }
        )
        flash('Thanks for registration! Please Login to continue','registerationProcess')

def sendConfirmationEmail():
    if request.method == 'POST':
        user = users_db.find_one({"email": str.lower(session['email'])})
        user1 = users_db.find_one({"rollno": session['rollno']})
        user2 = users_db.find_one({"contact": session['contact']})
        thapar_verify = str.lower((session['email'].split('@'))[1])
        print(thapar_verify,session['email'])
        if user or user1 or user2 or thapar_verify!='thapar.edu':
            if user:
                flash("Email already exists!",'registerationProcess')
            if (thapar_verify != 'thapar.edu'):
                flash("Please use thapar id",'registerationProcess')
            if user1:
                flash("Roll No already exists!",'registerationProcess')
            if user2:
                flash("Contact already exists!",'registerationProcess')
        else:
            OTP = generateOTP()
            msg = Message("Hostel Complaints registeration",
            sender = "dawarmuskan21@gmail.com",
            recipients = [session['email']])
            msg.body = f"The OTP for your session is {OTP}"
            mail.send(msg)
            return OTP

def generateOTP():
    otp=""
    for i in range(4):
        otp+=str(r.randint(1,9))
    print ("Your One Time Password is ")
    return otp


############################################### Complaint page ####################################################


@user_blueprint.route('/details',methods=['GET', 'POST'])
def details():    
    user = users_db.find_one({'email':session['email']})
    complaints = complaints_db.find({"rollno":user['rollno']})
    print(complaints[0],session['email'])
    return render_template('user/complaints.html',complaints = complaints)

def datetimeToReadable(timestamp):
    return datetime.fromtimestamp(timestamp)
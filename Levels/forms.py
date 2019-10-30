from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField,IntegerField,PasswordField)
from wtforms.validators import InputRequired,EqualTo,Email
from wtforms.fields.html5 import EmailField
class Registration(FlaskForm):
    email = EmailField("Email",validators = [InputRequired("Please enter your Email address"),Email("Please enter a valid Email address")])
    rollno = IntegerField("Roll no ",validators = [InputRequired("Please enter your Roll No.")])
    hostel = SelectField(u'Hostel',choices=[('A', 'A'), ('B', 'B'),('C', 'C'),('D', 'D'),('E', 'E'),('F', 'F'),('G', 'G'),('H', 'H'),('I', 'I'),('J', 'J'),('K', 'K'),('L', 'L'),('M', 'M'),('N', 'N'),('FRD', 'FRD')])
    roomno = IntegerField("Room no. ",validators = [InputRequired("Please enter your Room No.")])
    password = PasswordField("Password ",validators=[InputRequired("Please enter a password"),EqualTo('pass_confirm',message="Passwords don't match!!")])
    pass_confirm = PasswordField("Confirm Password",validators = [InputRequired("Re-enter the password to confirm")])
    contact = IntegerField("Contact No.",validators = [InputRequired("Please enter your contact number")])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = EmailField("Email",validators = [InputRequired("Please enter your Email address"),Email("Please enter a valid Email address")])
    password = PasswordField("Password ",validators=[InputRequired("Please enter your password")])
    submit = SubmitField('Login')

class otpForm(FlaskForm):
    OTP = StringField(validators=[InputRequired("Please enter your OTP")])
    submit = SubmitField('Verify')

class ComplaintForm(FlaskForm):
    complaint_type = SelectField('complaint_type',choices = [('general','general'),('room_specific','room_specific')])
    subject = StringField('subject',validators=[InputRequired('Enter subject')])
    complaint_desc = TextAreaField('complaint',validators=[InputRequired('Write your complaint')])
    submit = SubmitField('Register Complaint')

class CaretakerLoginForm(FlaskForm):
    caretaker_email = EmailField("Email",validators = [InputRequired("Please enter your Email address"),Email("Please enter a valid Email address")])
    caretaker_password = PasswordField("Password ",validators=[InputRequired("Please enter your password")])
    submitCaretaker = SubmitField('Login')

class adminLoginForm(FlaskForm):
    admin_email = EmailField("Email",validators = [InputRequired("Please enter your Email address"),Email("Please enter a valid Email address")])
    admin_password = PasswordField("Password ",validators=[InputRequired("Please enter your password")])
    submitadmin = SubmitField('Login')
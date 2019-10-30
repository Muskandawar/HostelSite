from Levels import app
app.run(debug=True)
# from Levels import app, mongo, users
# from flask import render_template,url_for,session,redirect,flash, abort,request
# from Levels.forms import Registration,LoginForm
# from flask_login import login_user, login_required, logout_user
# from flask_pymongo import PyMongo
# from Levels.user.authenticate import register, login, logout

# @app.route('/',methods=['GET', 'POST'])
# def index():
#     form = Registration()
#     form2 = LoginForm()
#     if form.validate_on_submit():
#         session['email'] = form.email.data
#         session['rollno'] = form.rollno.data
#         session['hostel'] = form.hostel.data
#         session['roomno'] = form.roomno.data
#         session['password'] = form.password.data
#         session['contact'] = form.contact.data
#         register(session)
#         return redirect(url_for('index'))
    
#     elif form2.validate_on_submit():
#         session['email'] = form2.email.data
#         session['password'] = form2.password.data
#         return redirect(url_for('login'))
#     return render_template('index.html',form=form)


# if __name__ == '__main__':
#     app.run(debug=True)
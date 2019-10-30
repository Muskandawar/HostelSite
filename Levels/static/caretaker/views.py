from flask import Blueprint, render_template, redirect, url_for

caretaker_blueprint = Blueprint('caretaker',__name__, template_folder='templates', static_folder='static')

@caretaker_blueprint.route('/',methods=['GET', 'POST'])
def Login():
    return render_template('caretaker/index.html')
from flask import Blueprint, render_template, redirect, url_for

admin_blueprint = Blueprint('admin',__name__, template_folder='templates',static_folder='static')

@admin_blueprint.route('/',methods=['GET', 'POST'])
def Login():
    return render_template('admin/admin_dashboard.html')
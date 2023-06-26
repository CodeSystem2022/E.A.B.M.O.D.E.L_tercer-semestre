from flask import render_template, request, redirect, url_for
from flask import Blueprint
 
from flask import session
logout = Blueprint('logout', __name__, template_folder='templates')

# Devuelve  los ultimos 10 lotes ingresados al sistema
@logout.route('/logout', methods=['GET'])
def getall():
    session.clear()
    return redirect(url_for('login.getall'))
       
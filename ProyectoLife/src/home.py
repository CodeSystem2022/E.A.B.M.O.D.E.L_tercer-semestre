from datetime import datetime
from decouple import config
import requests

from flask import (
    flash,
    render_template,
    request,
    session,
    redirect,
    url_for,
    Blueprint,
)



home = Blueprint('home', __name__, template_folder='templates')

@home.route('/home', methods=['GET', 'POST'])
def getall():
    if request.method == 'POST':
        sexo = request.form['gender']
        altura = request.form['altura']
        edad = request.form['edad']
        print(sexo)
        print(altura)
        print(edad)
        
    # Verificamos que la sesion no sea nula
    if session.get('user_id') is None:
        return redirect(url_for('login.getall'))


    return render_template('home.html')

from datetime import datetime
from decouple import config

from flask import (
    flash,
    render_template,
    request,
    session,
    redirect,
    url_for,
    Blueprint,
)



peso_ideal = Blueprint('peso_ideal', __name__, template_folder='templates')

@peso_ideal.route('/peso_ideal', methods=['POST'])
def getall():
    if request.method == 'POST':
        altura = request.form['altura']
        edad = request.form['edad']
        sexo = request.form['gender']
        print(sexo)
    return "recibi"
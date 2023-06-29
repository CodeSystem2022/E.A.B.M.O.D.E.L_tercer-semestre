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

from sqlalchemy import  text
import requests

login = Blueprint('login', __name__, template_folder='templates')

@login.route('/', methods=['GET', 'POST'])
def getall():
    from app import db
    if request.method == 'POST':
        # obtenemos los datos del formulario
        email = request.form['email']
        password = request.form['password']

        # insertamos los datos en la db
        query = text("SELECT * FROM usuarios WHERE email = :email")

        # ejecutamos la query
        result = db.session.execute(query, {"email": email})

        # obtenemos el resultado
        user = result.fetchone()

        if user is not None:
            error = False
            if(user.contraseña == password):
                session['user_id'] = user.id
                session['nombre'] = user.nombre
                return redirect(url_for('home.getall', nombre=user.nombre))
            else:
                error = True
        else:
            error = True

        return render_template('login.html', error=error)

    return render_template('login.html', error=False)
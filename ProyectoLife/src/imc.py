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



imc = Blueprint('imc', __name__, template_folder='templates')

@imc.route('/imc', methods=['POST'])
def getall():
    if request.method == 'POST':
        from app import db
        try:
            altura = request.form['altura']
            fecha_nacimiento = request.form['edad']
            sexo = request.form['gender']
            peso = request.form['peso']
            id_usuario = session['user_id']

            edad = datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()
            edad = int(datetime.now().year - edad.year)
            estatura_metros = int(altura) / 100  # Convertir estatura a metros
            imc = int(peso) / (estatura_metros ** 2)
            imc = round(imc, 2)
            # enviamos el peso ideal a la db
            query = text("INSERT INTO imc (id_usuario, sexo, edad, altura, peso, imc) VALUES (:id_usuario, :sexo, :edad, :altura, :peso, :imc)")
            db.session.execute(query, {"id_usuario": id_usuario, "sexo": sexo, "edad": fecha_nacimiento, "altura": altura, "peso": peso, "imc": imc})
            db.session.commit()
            return render_template('home.html', imc=imc)
        except:
            return render_template('home.html', error_imc=True)

    return render_template('home.html', )
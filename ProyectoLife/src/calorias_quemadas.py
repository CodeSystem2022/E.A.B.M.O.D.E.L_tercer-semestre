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


calorias_quemadas = Blueprint('calorias_quemadas', __name__, template_folder='templates')

@calorias_quemadas.route('/calorias_quemadas', methods=['POST'])
def getall():
    if request.method == 'POST':
        try:
            from app import db
            peso = float(request.form['peso'])
            altura = float(request.form['altura'])
            fecha_nacimiento = request.form['edad']
            sexo = request.form['gender']
            actividad = float(request.form['actividad'])/100
            diasemana = request.form['diasemana']

            edad = datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()
            edad = float(datetime.now().year - edad.year)

            if sexo == 'male':
                calorias_quemadas = (10 * peso) + (6.25 * altura) - (5 * edad) + (5 * actividad)
                calorias_quemadas = round(calorias_quemadas, 2)

            elif sexo == 'female':
                calorias_quemadas = (10 * peso) + (6.25 * altura) - (5 * edad) - (161 * actividad)
                calorias_quemadas = round(calorias_quemadas, 2)

            else:
                return render_template('home.html')
            
            query = text("INSERT INTO calorias_quemadas (id_usuario, sexo, edad, altura, peso, actividad, calorias_quemadas, dia_semana) VALUES (:id_usuario, :sexo, :edad, :altura, :peso, :actividad, :calorias_quemadas, :dia_semana)")
            db.session.execute(query, {"id_usuario": session['user_id'], "sexo": sexo, "edad": fecha_nacimiento, "altura": altura, "peso": peso,
                                       "actividad": actividad, "calorias_quemadas": calorias_quemadas, "dia_semana": diasemana})
            db.session.commit()
            return render_template('home.html', calorias_quemadas=calorias_quemadas)
        except:
            return render_template('home.html', error_calorias_quemadas=True)

    return render_template('home.html')
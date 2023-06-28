import os
import json
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
    jsonify
)
from sqlalchemy import text

calorias_quemadas_user = Blueprint('calorias_quemadas_user', __name__, template_folder='templates')

@calorias_quemadas_user.route('/calorias_quemadas_user', methods=['GET'])
def getall():
    usuario_calorias_quemadas = {}
    from app import db
    # Obtenemos las calorias quemadas del usuario
    query = text("SELECT * FROM calorias_quemadas WHERE id_usuario = :id_usuario ORDER BY id DESC LIMIT 7")
    result = db.session.execute(query, {"id_usuario": session['user_id']})
    datos_usuario = result.fetchall()

    for data in datos_usuario:
        edad = int(datetime.now().year - data.edad.year)
        # Convertimos de formato int a string los días
        dias_semana = {
            0: 'Domingo',
            1: 'Lunes',
            2: 'Martes',
            3: 'Miércoles',
            4: 'Jueves',
            5: 'Viernes',
            6: 'Sábado'
        }

        dia = dias_semana[data.dia_semana]
        # Guardamos todos los datos en formato diccionario
        usuario_calorias_quemadas[data.dia_semana]= {"user_id":data.id_usuario, "sexo":data.sexo, "edad":edad, "peso":data.peso, "altura":data.altura, "actividad":data.actividad, "calorias_quemadas":data.calorias_quemadas, "dia":dia}
    # Enviamos al home
    return render_template('home.html', nombre=session['nombre'], usuario_calorias_quemadas=usuario_calorias_quemadas)

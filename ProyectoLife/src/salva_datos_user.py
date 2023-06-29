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

salva_datos_user = Blueprint('salva_datos_user', __name__, template_folder='templates')

@salva_datos_user.route('/salva_datos_user', methods=['GET'])
def getall():
    usuario_calorias_quemadas = {}
    usuario_imc = {}
    from app import db
    # Obtenemos las calorias quemadas del usuario
    query = text("SELECT * FROM calorias_quemadas WHERE id_usuario = :id_usuario ORDER BY id DESC LIMIT 7")
    result = db.session.execute(query, {"id_usuario": session['user_id']})
    datos_usuario = result.fetchall()

    dias_semana = {
        0: 'Domingo',
        1: 'Lunes',
        2: 'Martes',
        3: 'Miércoles',
        4: 'Jueves',
        5: 'Viernes',
        6: 'Sábado'
    }

    for data in datos_usuario:
        edad = int(datetime.now().year - data.edad.year)
        # Convertimos de formato int a string los días

        dia = dias_semana[data.dia_semana]
        # Guardamos todos los datos en formato diccionario
        usuario_calorias_quemadas[data.dia_semana]= {"user_id":data.id_usuario, "sexo":data.sexo,
                                                     "edad":edad, "peso":data.peso, "altura":data.altura,
                                                     "actividad":data.actividad, "calorias_quemadas":data.calorias_quemadas,
                                                     "dia":dia}
        
    # Traemos el IMC
    query = text("SELECT * FROM imc WHERE id_usuario = :id_usuario ORDER BY id DESC LIMIT 7")
    result = db.session.execute(query, {"id_usuario": session['user_id']})
    datos_usuario = result.fetchall()
    for data in datos_usuario:
        edad = int(datetime.now().year - data.edad.year)

        dia = dias_semana[data.dia_semana]
        # Guardamos todos los datos en formato diccionario
        usuario_imc[data.dia_semana] = {"user_id":data.id_usuario, "sexo":data.sexo,
                       "edad":edad, "peso":data.peso, "altura":data.altura,
                       "imc":data.imc, "dia":dia}

    # Retornamos los datos en formato JSON
    return jsonify({
        "usuario_calorias_quemadas": usuario_calorias_quemadas,
        "usuario_imc": usuario_imc
    })
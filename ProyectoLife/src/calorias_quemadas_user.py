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
)
from sqlalchemy import  text

calorias_quemadas_user = Blueprint('calorias_quemadas_user', __name__, template_folder='templates')

@calorias_quemadas_user.route('/calorias_quemadas_user', methods=['GET'])
def getall():
    from app import db
    # Recuperar todos los registros de la tabla para el usuario actual
    query = text("SELECT * FROM calorias_quemadas WHERE id_usuario = :user_id")
    result = db.session.execute(query, {"user_id": session['user_id']})
    records = result.fetchall()

    # Convertir los registros a una lista de diccionarios
    records_list = []
    for record in records:
        record_dict = {
            'id_usuario': record.id_usuario,
            'sexo': record.sexo,
            'edad': record.edad,
            'altura': record.altura,
            'peso': record.peso,
            'actividad': record.actividad,
            'calorias_quemadas': record.calorias_quemadas,
            'dia_semana': record.dia_semana
        }
        records_list.append(record_dict)

    # Convertir la lista de diccionarios a una cadena JSON
    json_data = json.dumps(records_list)

    # Guardar el JSON en un archivo dentro de la carpeta "temporal"
    folder_path = "temporal"
    os.makedirs(folder_path, exist_ok=True)  # Crear la carpeta si no existe
    file_path = os.path.join(folder_path, "calorias_quemadas.json")

    with open(file_path, 'w') as file:
        file.write(json_data)

    return 200
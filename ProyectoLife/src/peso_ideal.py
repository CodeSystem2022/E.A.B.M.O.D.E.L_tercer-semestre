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



peso_ideal = Blueprint('peso_ideal', __name__, template_folder='templates')

@peso_ideal.route('/peso_ideal', methods=['POST'])
def getall():
    if request.method == 'POST':
        try:
            from app import db
            altura = request.form['altura']
            fecha_nacimiento = request.form['edad']
            sexo = request.form['gender']
            id_usuario = session['user_id']

            edad = datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()
            edad = int(datetime.now().year - edad.year)
            
            # Calculo de peso ideal
            if sexo == 'male':
                peso_ideal = (int(altura) - 100 + int(edad)/10) * 0.9
                peso_ideal = round(peso_ideal, 2)
            else:
                peso_ideal = (int(altura) - 100 + int(edad)/10) * 0.9 - 2.5
                peso_ideal = round(peso_ideal, 2)

            # enviamos el peso ideal a la db
            query = text("INSERT INTO peso_ideal (id_usuario, sexo, edad, altura, peso_ideal) VALUES (:id_usuario, :sexo, :edad, :altura, :peso_ideal)")
            db.session.execute(query, {"id_usuario": id_usuario, "sexo": sexo, "edad": fecha_nacimiento, "altura": altura, "peso_ideal": peso_ideal})
            db.session.commit()
        except:
            return render_template('home.html', error_peso_ideal=True)

    return render_template('home.html', peso_ideal=peso_ideal)
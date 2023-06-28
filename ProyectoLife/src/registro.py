from flask import (
    render_template,
    request,
    session,
    redirect,
    url_for,
    Blueprint,
)

from sqlalchemy import  text

registro = Blueprint('registro', __name__, template_folder='templates')

@registro.route('/registro', methods=['GET', 'POST'])
def getall():
    if request.method == 'POST':
        # conectamos con la db
        from app import db

        # obtenemos los datos del formulario
        nombre = request.form['name']
        apellido = request.form['lastName']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']
        # se deberia hacer validaciones pero por falta de 1 miembro del grupo no se pudo determinar quien lo hará

        # insertamos los datos en la db
        query = text("INSERT INTO usuarios (nombre, apellido, email, contraseña, confir_contraseña) VALUES (:nombre, :apellido, :email, :contraseña, :confir_contraseña)")

        # ejecutamos la query
        db.session.execute(query,{"nombre":nombre,"apellido":apellido, "email":email, "contraseña":password, "confir_contraseña":confirm_password})
        # guardamos los cambios
        db.session.commit()

        # redireccionamos a la pagina de login
        return redirect(url_for('login.getall'))

    return render_template('registro.html')

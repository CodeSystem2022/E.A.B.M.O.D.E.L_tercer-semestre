from flask import Flask, render_template, request
from scripts.DDBB import get_db
from flask_sqlalchemy import SQLAlchemy

from  src.home import home
from  src.login import login
from  src.registro import registro


app = Flask(__name__)

# Conexion a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = get_db() # Realizamos la conexión
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Evitamos el warning
app.config['SQLALCHEMY_ECHO'] = False # Evitamos el warning

db = SQLAlchemy(app) # Inicializamos la base de datos

app.secret_key = 'lautneslamejorilovepython'

# Aca se registran los html / .py de cada uno
app.register_blueprint(home)
app.register_blueprint(login)
app.register_blueprint(registro)


if __name__=='__main__':
    app.run(debug=True)
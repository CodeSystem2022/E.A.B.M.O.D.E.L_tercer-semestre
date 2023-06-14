from flask import Flask, render_template, request
from  src.home import home


app = Flask(__name__)


app.secret_key = 'lautneslamejorilovepython'

# Aca se registran los html / .py de cada uno
app.register_blueprint(home)


if __name__=='__main__':
    app.run(debug=True)
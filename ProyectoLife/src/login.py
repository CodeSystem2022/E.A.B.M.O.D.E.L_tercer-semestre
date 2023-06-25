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

login = Blueprint('login', __name__, template_folder='templates')

@login.route('/', methods=['GET', 'POST'])
def getall():
    from app import db
    
    return render_template('login.html')

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



home = Blueprint('home', __name__, template_folder='templates')

@home.route('/home', methods=['GET', 'POST'])
def getall():
    
    return render_template('home.html')

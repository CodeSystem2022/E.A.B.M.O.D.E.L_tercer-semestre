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



register = Blueprint('register', __name__, template_folder='templates')

@register.route('/register', methods=['GET', 'POST'])
def getall():
    
    return render_template('register.html')

from flask import Blueprint, flash, redirect, url_for, render_template

from Oidc_Decorators import oidc
from LoggingHandler import logger

start = Blueprint('home', __name__, template_folder='templates')

@start.route('/')
def Startscreen():
    if oidc.user_loggedin:
        flash('Welcome %s' % oidc.user_getfield('username'))
        logger.info('Erfolgreich eingelogt und Weiterleitung zur Startseite')
        return redirect(url_for('dash.dashboard'))
    else:
        return render_template('startscreen.html')

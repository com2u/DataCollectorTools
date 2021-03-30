from Oidc_Decorators.Decorators import require_keycloak_role
from flask import Blueprint, flash, render_template, request
from flask import Blueprint, render_template, redirect, url_for, flash, session

from LoggingHandler import NickModul
from Oidc_Decorators import oidc

log = Blueprint('log', __name__,  static_folder='/static', static_url_path="/pages-static",
                 template_folder='templates')


@log.route('/loggingTest', methods=['POST', 'GET'])
@oidc.require_login
def logTest():
    if request.method == 'POST':
        number = int(request.values.get("number"))
        if number >= 0:
            NickModul.warning("You have a number higher than 10!")
            return redirect(url_for('log.logTest'))
        else:
            NickModul.warning("Your number is less than zero!")
            return redirect(url_for('log.logTest'))
    
    return '<form action="/loggingTest" method = "post" > <div> <input type="number" id ="number" name="number"> </div> <div> <button>Send number</button></div> </form>'

#welche Application
#datum Uhrzeit stempel
#log level

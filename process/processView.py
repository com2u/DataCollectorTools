import ast
import json
from db_actions import PostgersqlDBManagement, SQLiteDBManagement
from Oidc_Decorators.Decorators import require_keycloak_role
from flask import Blueprint, flash, render_template, request
from flask import Blueprint, render_template, redirect, url_for, flash, session


from Oidc_Decorators import oidc
from LoggingHandler import logger

process = Blueprint('process', __name__, template_folder='templates')


@process.route('/process', methods=['POST', 'GET'])
@oidc.require_login
def dashboard():

    if request.method == 'POST':
        
        #delete_function = form.
        pass


    return render_template('processPage.html')

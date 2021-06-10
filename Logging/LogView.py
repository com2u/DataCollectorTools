from flask import Blueprint, render_template, redirect, url_for, request, flash

import logging
from Oidc_Decorators import oidc

log = Blueprint('log', __name__,  static_folder='/static', static_url_path="/pages-static",
                 template_folder='templates')


def logging_intern():

    RequestLogging = logging

    LoggerIntern = RequestLogging.getLogger('DB-Tools')
    LoggerIntern.setLevel(10)

    ch = RequestLogging.StreamHandler()
    ch.setLevel(10)

    formatter = RequestLogging.Formatter(
        '%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    ch.setFormatter(formatter)
    LoggerIntern.addHandler(ch)

    return LoggerIntern


def logging_server():
    from Logging.LogHandler import SVLog
    RequestLogging = SVLog()

    LoggerExtern = RequestLogging.getLogger('DB-Tools-Server-Logging')
    LoggerExtern.setLevel(10)

    ch = RequestLogging.StreamHandler()
    ch.setLevel(10)

    formatter = RequestLogging.Formatter(
        '%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    ch.setFormatter(formatter)
    LoggerExtern.addHandler(ch)
    return LoggerExtern


@log.route('/loggingDecision', methods=['POST', 'GET'])
@oidc.require_login
def logDecision():
    if request.method == 'POST':
        
        LogClient = request.values['LogClient']
        #LogServer = request.form['LogServer']

        if LogClient == 'Yes':
            from Logging import ClientLogger
            ClientLogger.setLevel(logging.CRITICAL + 1)

        elif LogClient == 'No':
            from Logging import ClientLogger
            ClientLogger.setLevel(logging.DEBUG)

        return redirect(url_for('dash.dashboard'))
    
    return render_template('loggingDecision.html')

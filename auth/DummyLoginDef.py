from flask import Blueprint, redirect, url_for, session, request, session
import os
import json
from base64 import urlsafe_b64encode
from flask import current_app
from itsdangerous import JSONWebSignatureSerializer
from six.moves.urllib.parse import urlencode
import re
import mechanize
import requests

from Oidc_Decorators import oidc


def redirect_to_auth_server():
    destination = request.url

    if 'oidc_csrf_token' not in session:
        csrf_token = urlsafe_b64encode(os.urandom(24)).decode('utf-8')
        session['oidc_csrf_token'] = csrf_token
    state = {
        'csrf_token': session['oidc_csrf_token'],
    }

    statefield = 'destination'
    statevalue = destination

    state[statefield] = oidc.extra_data_serializer.dumps(
        statevalue).decode('utf-8')

    extra_params = {
        'state': urlsafe_b64encode(json.dumps(state).encode('utf-8')),
    }

    #extra_params.update(current_app.config['OIDC_EXTRA_REQUEST_AUTH_PARAMS'])
    if current_app.config['OIDC_GOOGLE_APPS_DOMAIN']:
        extra_params['hd'] = current_app.config['OIDC_GOOGLE_APPS_DOMAIN']
    if current_app.config['OIDC_OPENID_REALM']:
        extra_params['openid.realm'] = current_app.config['OIDC_OPENID_REALM']

    flow = oidc.flow_for_request()
    auth_url = '{url}&{extra_params}'.format(
        url=flow.step1_get_authorize_url(),
        extra_params=urlencode(extra_params))
    # if the user has an ID token, it's invalid, or we wouldn't be here
    oidc.set_cookie_id_token(None)
    return auth_url

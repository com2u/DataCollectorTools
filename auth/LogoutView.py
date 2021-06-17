from flask import Blueprint, redirect, url_for, session, request, session
import os
import json
from base64 import urlsafe_b64encode
from flask import current_app
from itsdangerous import JSONWebSignatureSerializer
from six.moves.urllib.parse import urlencode



from Oidc_Decorators import oidc

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/logout', methods=['GET', 'POST'])
@oidc.require_login
def logout():
    oidc.logout()
    session.clear()
    return redirect('http://localhost:8080/auth/realms/DBTools/protocol/openid-connect/logout?redirect_uri=http://localhost:5000/')

@auth.route('/dummy_login', methods= ['GET', 'POST'])
def dummy_login():

    session.clear()
    oidc._before_request
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
    print(auth_url)

    username = "tester1"
    password = "12345"

    PATH = "C:\Program Files (x86)\chromedriver.exe"

    # initialize the Chrome driver
    driver = webdriver.Chrome(PATH)

    # head to github login page
    driver.get(str(auth_url))
    # find username/email field and send the username itself to the input field
    driver.find_element_by_id("username").send_keys(username)
    # find password input field and insert password as well
    driver.find_element_by_id("password").send_keys(password)
    # click login button
    driver.find_element_by_id("kc-login").click()
    driver.close()
    '''
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.open(auth_url)
    #kc-login for submit button
    br.select_form(nr=0)
    br.form['username'] = 'tester1'
    br.form['password'] = '12345'
    br.submit
    '''

    oidc._after_request

    return redirect(url_for('auth.test'))



@auth.route('/test', methods=['GET', 'POST'])
@oidc.require_login
def test():
    return redirect(url_for('dash.dashboard'))

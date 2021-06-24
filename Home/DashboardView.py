from flask import Blueprint, render_template, redirect, url_for

from Oidc_Decorators import oidc

dash = Blueprint('dash', __name__,  static_folder='/static', static_url_path="/pages-static",
                 template_folder='templates')

@dash.route('/home/', methods=['POST', 'GET'])
@oidc.require_login
def dashboard():
    if oidc.user_loggedin:
        return render_template('homepage.html')
      
    return redirect(url_for('start.Startscreen'))

import json
from base64 import b64decode
from functools import wraps
from flask import redirect, url_for, flash
from flask.helpers import make_response

from Oidc_Decorators import oidc
from LoggingHandler import logger

def require_keycloak_role(roles):
    """
        Function to check for a KeyCloak client role in JWT access token.
        This is intended to be replaced with a more generic 'require this value
        in token or claims' system, at which point backwards compatibility will
        be added.
        :param role: A single role or a list of roles that are required. Used to check if the logged_in user has those specific requirements
        :type scopes_required: list or a string
        :returns: True if the specific role was inisde the users realm-settings. 
            An ErrStr (subclass of string for which bool() is False) if
            an error occured.
        :rtype: Boolean or String
    """
    def wrapper(view_func):
        @wraps(view_func)
        def decorated(*args, **kwargs):
            raw_access_token = oidc.get_access_token()
            pre, tkn, post = raw_access_token.split('.')
            access_token = b64decode(tkn + '=' * (-len(tkn) % 4))
            access_token = json.loads(access_token.decode('utf-8'))

            user_id = oidc.user_getfield('sub')
            access_token_id = access_token['sub']

            if oidc.validate_token(raw_access_token) and (user_id == access_token_id):
                for role in roles:
                    if role in access_token['realm_access']['roles']:
                        logger.info('Rolle erfolgreich im AccessToken des aktuellen Benutzers. Zugang zur Seite erlaubt')
                        return view_func(*args, **kwargs)
                else:
                    logger.warning('Unauthorized User! Zugang zur Seite verweigert')
                    flash('Unauthorized!', 'danger')
                    return redirect(url_for('dash.dashboard')) 
            else: 
                logger.warning('Token invalid!')
                flash('Invalid Token!', 'danger')
                return redirect(url_for('dash.dashboard'))
        return decorated
    return wrapper

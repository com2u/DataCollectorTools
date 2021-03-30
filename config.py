"""Flask app configuration."""
import json


class Config:
    """Set Flask configuration from environment variables."""


    DEBUG = False
    FLASK_APP = 'app.py'
    SECRET_KEY = str((json.load(open('.\client_secrets.json')))["SECRET_KEY"])
    OIDC_CLIENT_SECRETS = '.\client_secrets.json'
    OIDC_ID_TOKEN_COOKIE_SECURE = False
    OIDC_VALID_ISSUERS = ['http://localhost:8080/auth/realms/Application1']
    OIDC_SCOPES = ['openid', 'email', 'profile']
    OIDC_INTROSPECTION_AUTH_METHOD = 'client_secret_post'
    OIDC_CLOCK_SKEW = 560

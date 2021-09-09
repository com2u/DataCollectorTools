import sass, os, json


def generate_env():
    generate_css()
    generate_client_secrets_json()


def generate_css():
    sass.compile(dirname=('static/styles/scss',
                 'static/styles/Bootstrap/css/'), output_style='compressed')
    """Create Flask application."""


def generate_client_secrets_json(client_secret=""):
    secrets_json = {
        "web": {
            "issuer": f"http://{os.getenv('KEYCLOAK_IP')}:8080/auth/realms/DBTools",
            "auth_uri": f"http://{os.getenv('KEYCLOAK_IP')}:8080/auth/realms/DBTools/protocol/openid-connect/auth",
            "client_id": f"FrontendApp",
            "client_secret": f"{client_secret}",
            "redirect_uris": [
                f"http://{os.getenv('KEYCLOAK_IP')}:5000/*"
            ],
            "userinfo_uri": f"http://{os.getenv('KEYCLOAK_IP')}:8080/auth/realms/DBTools/protocol/openid-connect/userinfo",
            "token_uri": f"http://{os.getenv('KEYCLOAK_IP')}:8080/auth/realms/DBTools/protocol/openid-connect/token",
            "token_introspection_uri": f"http://{os.getenv('KEYCLOAK_IP')}:8080/auth/realms/DBTools/protocol/openid-connect/token/introspect"
        },
        "SECRET_KEY": f"123456789123456789",
        "OIDC_VALID_ISSUERS": f"http://{os.getenv('KEYCLOAK_IP')}:8080/auth/realms/DBTools",
        "REALM-NAME": f"DBTools"
    }
    with open("client_secrets.json", "w" ) as  secrets_json_file:
        json.dump(secrets_json, secrets_json_file)
    return secrets_json


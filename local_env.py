import sass
import os
import json
import requests
import sys
import time
import psycopg2
from timeit import default_timer as timer
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def generate_env():
    generate_css()
    configure_pg_connection()
    configure_keycloak()
    generate_client_secrets_json()


def generate_css():
    sass.compile(dirname=('static/styles/scss',
                 'static/styles/Bootstrap/css/'), output_style='compressed')
    """Create Flask application."""


def generate_client_secrets_json():
    secrets_json = {
        "web": {
            "issuer": f"http://{os.getenv('KEYCLOAK_IP', '127.0.0.1')}:8080/auth/realms/{os.getenv('KEYCLOAK_REALM_NAME', 'DBTools')}",
            "auth_uri": f"http://{os.getenv('KEYCLOAK_IP', '127.0.0.1')}:8080/auth/realms/{os.getenv('KEYCLOAK_REALM_NAME', 'DBTools')}/protocol/openid-connect/auth",
            "client_id": f"{os.getenv('KEYCLOAK_CLIENT_NAME', 'FrontendApp')}",
            "client_secret": f"",
            "redirect_uris": [
                f"http://{os.getenv('KEYCLOAK_IP', '127.0.0.1')}:5000/*"
            ],
            "userinfo_uri": f"http://{os.getenv('KEYCLOAK_IP', '127.0.0.1')}:8080/auth/realms/{os.getenv('KEYCLOAK_REALM_NAME', 'DBTools')}/protocol/openid-connect/userinfo",
            "token_uri": f"http://{os.getenv('KEYCLOAK_IP', '127.0.0.1')}:8080/auth/realms/{os.getenv('KEYCLOAK_REALM_NAME', 'DBTools')}/protocol/openid-connect/token",
            "token_introspection_uri": f"http://{os.getenv('KEYCLOAK_IP', '127.0.0.1')}:8080/auth/realms/{os.getenv('KEYCLOAK_REALM_NAME', 'DBTools')}/protocol/openid-connect/token/introspect"
        },
        "SECRET_KEY": f"123456789123456789",
        "OIDC_VALID_ISSUERS": f"http://{os.getenv('KEYCLOAK_IP', '127.0.0.1')}:8080/auth/realms/{os.getenv('KEYCLOAK_REALM_NAME', 'DBTools')}",
        "REALM-NAME": f"{os.getenv('KEYCLOAK_REALM_NAME', 'DBTools')}"
    }
    with open("client_secrets.json", "w") as secrets_json_file:
        json.dump(secrets_json, secrets_json_file)
    return secrets_json


def configure_keycloak(timeout_seconds=300):
    data = {
        "client_id": "admin-cli",
        "username": f"{os.getenv('KEYCLOAK_USER', 'admin')}",
        "password": f"{os.getenv('KEYCLOAK_PASSWORD', 'admin')}",
        "grant_type": "password"
    }
    response = None
    start_time = timer()
    while response is None:
        try:
            response = requests.post(
                f"http://{os.getenv('KEYCLOAK_IP', '127.0.0.1')}:8080/auth/realms/master/protocol/openid-connect/token", data)
        except:
            if (timer() - start_time > timeout_seconds):
                sys.exit(
                    f"could not establish connection to keycloak server after {timeout_seconds}s at {os.getenv('KEYCLOAK_IP', '127.0.0.1')}\n exiting")
            time.sleep(2)
            pass
    access_token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {access_token}"}
    # checking if Realm allready exsists
    response = requests.get(
        f"http://{os.getenv('KEYCLOAK_IP', '127.0.0.1')}:8080/auth/admin/realms", headers=headers)
    realms = response.json()
    realm_ids = [realm['id'] for realm in realms]
    if os.getenv('KEYCLOAK_REALM_NAME', 'DBTools') not in realm_ids:
        # creating new realm with Client
        realm_export_json = json.loads(open(
            "./docker/keycloak/dbtools-realm-export.json", "r").read().replace(f"http://localhost:5000/", f"http://{os.getenv('KEYCLOAK_IP')}:5000/"))

        response = requests.post(
            f"http://{os.getenv('KEYCLOAK_IP', '127.0.0.1')}:8080/auth/admin/realms", headers=headers, json=realm_export_json)
    # check for Users
    response = requests.get(
        f"http://{os.getenv('KEYCLOAK_IP', '127.0.0.1')}:8080/auth/admin/realms/{os.getenv('KEYCLOAK_REALM_NAME', 'DBTools')}/users", headers=headers)
    users = [user["username"] for user in response.json()]
    if "tester" not in users:
        user_info = {
            "username": "tester",
            "enabled": True,
            "emailVerified": False,
            "credentials": [
                {
                    "type": "password",
                    "value": "tester",
                    "temporary": False
                }
            ]
        }
        response = requests.post(
            f"http://{os.getenv('KEYCLOAK_IP', '127.0.0.1')}:8080/auth/admin/realms/{os.getenv('KEYCLOAK_REALM_NAME', 'DBTools')}/users", headers=headers, json=user_info)
    return ""


def configure_pg_connection():
    try:
        conn = psycopg2.connect(
            f"user='{os.getenv('DEFAULT_DATABASE_USER')}' host='{os.getenv('DEFAULT_DATABASE_ADDR')}' password='{os.getenv('DEFAULT_DATABASE_PASSWORD')}' connect_timeout=1 ")
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute("SELECT datname FROM pg_database")
        databases = [datname[0] for datname in cur.fetchall()]
        if f"{os.getenv('DATABASE_NAME_DBTOOLS')}" not in databases:
            cur.execute(f"CREATE DATABASE {os.getenv('DATABASE_NAME_DBTOOLS')}")
        cur.close()
        conn.close()
    except (Exception, psycopg2.Error) as error:
        sys.exit("Error whily trying to set up Postgres environment")
    finally:
        if conn:
            cur.close()
            conn.close()
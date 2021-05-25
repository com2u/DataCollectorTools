from Oidc_Decorators import oidc
from Oidc_Decorators.Decorators import require_keycloak_role


def check_delete_permission():
    
    user_allowed_delete_data = False
    if require_keycloak_role(["Admin"]):
        user_allowed_delete_data = True

    return user_allowed_delete_data

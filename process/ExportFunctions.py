from Oidc_Decorators import oidc


@oidc.require_login
def exportData():
    pass


@oidc.require_login
def exportPictures():
    pass


@oidc.require_login
def enable_write_protection():
    #add a new function to db_actions.py
    #which is add a column
    # this is then called write_protected

    write_protected = False

    if write_protected == False:
        #call the function to add column write protection
        pass

    pass

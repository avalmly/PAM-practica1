def pam_sm_authenticate(pamh, flags, argv):
    pin = str(input('Ingrese PIN: '))
    if (pin == '1234'):
        return pamh.PAM_SUCCESS
    return pamh.PAM_AUTH_ERR    #Cambiar variable por una apropiada
    
def pam_sm_setcred(pamh, flags, argv):
    return pamh.PAM_SUCCESS

def pam_acct_mgmt(pamh, flags, argv):
    return pamh.PAM_SUCCESS

def pam_sm_open_session(pamh, flags, argv):
    return pamh.PAM_SUCCESS

def pam_sm_close_session(pamh, flags, argv):
    return pamh.PAM_SUCCESS

def pam_sm_chauthtok(pamh, flags, argv):
    return pamh.PAM_SUCCESS

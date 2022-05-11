import os
def runscript(new_password, ip_addr):
    x = os.system('./_Logan/default_cred/EXP-defaultcred.exp {} {}'.format(new_password, ip_addr))
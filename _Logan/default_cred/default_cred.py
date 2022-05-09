import os
import pexpect
def runscript(new_password):
    x = os.system('./_Logan/default_cred/EXP-defaultcred.exp {}'.format(new_password))
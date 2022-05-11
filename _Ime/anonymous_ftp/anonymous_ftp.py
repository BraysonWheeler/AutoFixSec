import os
import pexpect
def runscript(ip_addr):
    x = os.system('./_Ime/anonymous_ftp/EXP-anonymousftp.exp {}'.format(ip_addr))
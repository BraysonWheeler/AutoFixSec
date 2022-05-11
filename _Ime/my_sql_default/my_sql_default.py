import os
import pexpect
def runscript(new_password, ip_addr):
    x = os.system('./_Ime/my_sql_default/EXP-mysqldefault.exp {}'.format(new_password, ip_addr))
import os
import pexpect
def runscript(new_password):
    x = os.system('./_Ime/my_sql_default/EXP-mysqldefault.exp {}'.format(new_password))
import pandas as pd
import sys
import os
import re
import ufw_firewall

#How Python handles file imports from other files
sys.path.append('./_Logan')
sys.path.append('./_Logan/default_cred')
sys.path.append('./_Logan/rsh')
sys.path.append('./_Logan/rlogin')
sys.path.append('./api-stuff')
sys.path.append('./gvm-scripts')

#Imported py files outside of root directory
import rsh
import rlogin
import default_cred
import gvm_get_report

def new_password_function():
    check = True
    new_password = "alskjdhasdkljhASDASD123123!!!"
    #new_password = input("[+]If a default user account password is found what would you like to change it to? \n[+]Requirements: password of atleast 12 characters with 1 one uppercase and 1 numeral character")
    SpecialSym=['!','@','#','$','%','^','&','*','(',')','_','-','+','=','[','{',']','}','\\','|',':',';','\'','\"',',','<','.','>','?','/']
    if len(new_password) < 12:
        print('[!]length should be at least 6')
        check = False
    if not any(char.isupper() for char in new_password):
        print('[!]Password should have at least one uppercase letter')
        check = False
    
    if not any(char.isdigit() for char in new_password):
        print('[!]Password should have at least one numeral')
        check = False
    if not any(char in SpecialSym for char in new_password):
        print('[!]the password should have at least one special character')
        check=False

    if not check:
        print('\n')
        new_password_function()
    else:  
        return new_password
    

    
def configure_firewall():
    ufw_firewall.setup()



def main():

    gvm_get_report.get_report() #Gets report of scan generates report in folder with main


    df = pd.read_csv('./Automated_export.csv',encoding='latin-1') #Pulls report generated

    #new_password = new_password_function() #IF default credentials are found replace with this passoword
    new_password = 'asd123'
    lst = []
    for index,row in df.iterrows():
        data=[]

        cvss = row['CVSS']
        if(cvss != cvss):
            cvss = 'None'

        severity = row['Severity']
        if(severity != severity):
            severity = 'None'

        solution_type = row['Solution Type']
        if(solution_type != solution_type):
            solution_type = 'None'

        solution = row['Solution']
        if(solution != solution):
            solution = 'None'

        affected = row['Affected Software/OS']
        if(affected != affected):
            affected = 'None'

        cve = row['CVEs']
        if(cve != cve):
            cve = 'None'

        nvtName = row['NVT Name']
        if(nvtName != nvtName):
            nvtName = 'None'


        data = [cvss,severity,solution_type,solution,affected,cve, nvtName]
        lst.append(data)

    print('Vulnerabilities found:')
    for i in lst:
        print(i[6])

    print('\n')

    ssh_ftp_default_credentials_found = False
    '''
    Had To be Removed Twitter's API has a limit for non enterprise accounts going through first vulnerability we ran out of space.
    print('Applying risk assesment')
    for i in lst:
        if i[5] != None :
            risk_score = twitterapi.score(i[5])
            print(risk_score)
    '''
    configure_firewall()
    for i in lst:
        if(i[6] == 'rlogin Passwordless Login'):
            os.system('./_Logan/rlogin/EXP-rlogin.exp')

        if(i[6] == 'rsh Unencrypted Cleartext Login'):
            os.system('./_Logan/rsh/EXP-rsh.exp')

        if(i[6] == 'SSH Brute Force Logins With Default Credentials Reporting'
                    or i[6] == 'FTP Brute Force Logins Reporting'
                    and ssh_ftp_default_credentials_found == False):

                        ssh_ftp_default_credentials_found = True
                        
        if(i[6] == 'Telnet Unencrypted Cleartext Login'):
            print(i)
            #x = os.system('./disableTelNet.exp')


    if ssh_ftp_default_credentials_found:
        default_cred.runscript(new_password)
main()
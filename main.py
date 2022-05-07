import pandas as pd
import os
import sys
#How Python handles file imports from other files
sys.path.append('./_Logan')
import cli
cli.runscript()

'''

#import twitterapi #TODO Import files from other files
#test
df = pd.read_csv('./telnet.csv',encoding='latin-1')

def main():
    print(main)
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

for i in lst:
    if(i[6] == 'Telnet Unencrypted Cleartext Login'):
        x = os.system('./disableTelNet.exp')
#score = twitterapi.score('CVE-2022-22965')
print(lst[0])

'''
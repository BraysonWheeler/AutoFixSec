import pandas as pd
import twitterapi
import gvmtools

import sys
from gvm.connections import UnixSocketConnection
from gvm.errors import GvmError
from gvm.protocols.gmp import Gmp
from gvm.transforms import EtreeCheckCommandTransform


username = 'admin'
password = '02169f70-676c-4789-8bad-8242fe85bd33'

connection = UnixSocketConnection(path=None)
transform = EtreeCheckCommandTransform()
try:
    with Gmp(connection=connection, transform=transform) as gmp:
        gmp.authenticate(username, password)

        tasks = gmp.get_tasks(filter_string='owasp')

        for task in tasks.xpath('task'):
            print(task.find('name').text)

except GvmError as e:
    print('An error occurred', e)


df = pd.read_csv('./report.csv',encoding='latin-1')


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


    data = [cvss,severity,solution_type,solution,affected,cve]
    lst.append(data)


#score = twitterapi.score('CVE-2022-22965')
#print(score)


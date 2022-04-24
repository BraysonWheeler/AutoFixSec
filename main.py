import pandas as pd
import twitterapi

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
print(lst[1])


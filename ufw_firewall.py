
import os
import time
import re
x = os.system('nmap -sT -p- 192.168.1.181 > ./openports.txt')
def Initial_configuration():
    print('asd')
ifile = open('openports.txt', 'r')
lines = ifile.readlines()
line_holding_list = []
openport_regex = "([0-9]+\/tcp).*"
os.system('chmod +x ufw_enable_Firewall.exp')
os.system('./ufw_enable_Firewall.exp')


for line in lines:
    line_holding_list.append(line.strip())

for i in line_holding_list:
    regex_object = re.match(openport_regex,i)
    if(regex_object):
        connection_allow_string = str(regex_object[1])
        print(connection_allow_string)
        os.system('./ufw_firewall.exp {}'.format(connection_allow_string))

'''
for line in test:
    line_holding_lst.append(line.strip())


ifile = open('inetd.conf', 'r')


test = ifile.readlines()
line_holding_lst = []
for line in test:
    line_holding_lst.append(line.strip())

rlogin_regex = ".*(\.rlogind)"
rshd_regex = ".*(\.rshd)"
rexecd_regex = ".*(\.rexecd)"


inetConf_lst = []
for i in line_holding_lst:
    if(re.search(rlogin_regex, i) or re.search(rshd_regex, i) or re.search(rexecd_regex, i)):
        newstr = "#" + i
        inetConf_lst.append(newstr + "\n")
    else:

        inetConf_lst.append(i + "\n")


print(inetConf_lst)

ofile = open('inetd.conf', 'w')
ofile.writelines((inetConf_lst))

'''
import re
ifile = open('./_Logan/rlogin/inetd.conf', 'r')


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


import os
import re
def setup(ip_addr):
    x = os.system('nmap -sT -p- {} > ./openports.txt'.format(ip_addr))#Places user supplied port into commandline run nmap scan

    ifile = open('openports.txt', 'r') #Opens file with port list
    lines = ifile.readlines() #reads each line
    line_holding_list = [] #our port list
    openport_regex = "([0-9]+\/tcp).*" #Matches 22/tcp -? 123123123/tcp
    os.system('chmod +x ufw_enable_Firewall.exp') #give priv's to enable firewall expect script incase we dont already have them.
    os.system('./ufw_enable_Firewall.exp {}'.format(ip_addr)) #Enable firewall


    for line in lines: #Strip out lines then appen to our list that holds the cleanly stripped lines
        line_holding_list.append(line.strip())

    for i in line_holding_list:
        regex_object = re.match(openport_regex,i) #Find the ##/tcp group if it exist

        if(regex_object): #If the ##/tcp is found create a string  containing ##/tcp
            connection_allow_string = str(regex_object[1]) 
            
            
            os.system('./ufw_firewall.exp {} {}'.format(connection_allow_string, ip_addr)) # call firewall expect script with the rule we want to create and the port of vuln machine
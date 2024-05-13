Logan <br />
Harper <br />
Skandha <br />
Ime <br />

# Using the vdi provided in dropbox
https://www.dropbox.com/s/fkncg2rgr52ie9y/Kalix2.vdi?dl=0 Here is the virtual disk image of the machine I used to run the demo in our video. From the virtual disk image you can recreate my virtual machine. Will negate all future openvas configurations and dependency installs.

Metasploitable download:https://sourceforge.net/projects/metasploitable/



Start with most up to date Kali Live Boot ISO: https://www.kali.org/get-kali/#kali-live

Metasploitable 2: https://sourceforge.net/projects/metasploitable/

# Installing Openvas on KALI
1.`sudo su` <br />
2.`apt-get update && apt-get install`<br />
3.`apt-get install openvas`<br />
4.`gvm-setup`<br />
    [!] Kali by default might have postgres13 using the default port for openvas follow
    [!] Setup will take 15-30 minutes<br />
    [!] Your admin password will be generated during the setup <br />
5.`sudo runuser -u _gvm -- gvmd --create-user=admin2 --new-password=12345`<br />
6.`gvm-check-setup`<br />
7.`geenbone-fee-sync --type gvmd_data`<br />
8.`geenbone-fee-sync --type CERT`<br />
[!] If Config's are still not synced try: <br />
    `sudo runuser -u _gvm -- greenbone-nvt-sync`<br />
    `sudo runuser -u _gvm -- greenbone-scapdata-sync`<br />
    `sudo runuser -u _gvm -- greenbone-certdata-sync`<br />
    


# Running Code
1. `apt-get install expect`
2. `git clone {repo}` <br />
3. Import the follow python libaries: <br />
    `pip3 install python-gvm` <br />
    `pip3 install os` <br />
    `pip3 install pandas' <br />
    `pip3 install lxml` <br />
    `pip3 install CronTab` <br />



# starting the project
Before begining be sure to change the admin credentials in create-and-scan-host-all-in-one.py to your admin credentials. Unless you are using the VDI your admin credentials are the same
Important run everything as root `sudo su` before starting any script

1. Create the target and taks then tart the scan.
    python ./create-and-scan-host-all-in-one.py.
2. Wait till scan completion
3. Configure export report.
    - Navigate to your browser. Log into the openvas scanner at 127.0.0.1:9392.
    - Go to scans-> Report.
    - then click on the date of our newly created scan.
    - Grab the ID in the top right hand corner. will look something like 02169f70-676c-4789-8bad-8242fe85bd33.
    - And place it into the gvm_get_report.py report_id variable.
4. Generate report .csv
    python gvm_get_report
5. Run main.py
6. Set the new password you want if default or weak credentials are found
7. wait for mitigations to complete.
8. Rescan vulnerable machine to see difference.
    - Navigate to your browser. Log into the openvas scanner at 127.0.0.1:9392.
    - go to scans->tasks
    - click the start task icon of a side facing trianble of our original task.   

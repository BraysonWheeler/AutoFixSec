# 3560-projects
Start with most up to date Kali Live Boot ISO https://www.kali.org/get-kali/#kali-live


# Installing Openvas on KALI
1.`sudo su` <br />
2.`apt-get update && apt-get install`<br />
3.`apt-get install openvas`<br />
4.`gvm-setup`<br />
    [!] Kali by default might have postgres13 using the default port for openvas follow
    [!] Setup will take 15-30 minutes<br />
5.`sudo runuser -u _gvm -- gvmd --create-user=admin2 --new-password=12345`<br />
6.`gvm-check-setup`<br />
7.`geenbone-fee-sync --type gvmd_data`<br />
8.`geenbone-fee-sync --type CERT`<br />
[!] If Config's are still not synced try: <br />
    `sudo runuser -u _gvm -- greenbone-nvt-sync`<br />
    `sudo runuser -u _gvm -- greenbone-scapdata-sync`<br />
    `sudo runuser -u _gvm -- greenbone-certdata-sync`<br />
    


# Running Code
1.`git clone {repo}` <br />
2.Import the follow python libaries:
    

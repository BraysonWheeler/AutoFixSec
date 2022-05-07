# 3560-projects
Start with most up to date Kali Live Boot ISO https://www.kali.org/get-kali/#kali-live


<h1>Installing OpenVas in Kali</h1>
1. sudo su
2. apt-get update && apt-get install
3. apt-get install openvas
4.gvm-setup
    - Setup will take 15-30 minutes
5.Get libraries
6.gvm-check-setup
7. geenbone-fee-sync --type gvmd_data
8.geenbone-fee-sync --type CERT

Wait for feed to update. (Takes 15-20 minutes)
cd /var/log/gvm
tail -f gvmd.log to see update status

<h1>Running Project</h1>
1. git clone {repo}
2. Import the follow libaries:
    - 

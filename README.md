Proposal
Goal: Automation
Using Open Vas Vulnerability scanner we will scan a vulnerable vm. Export the vulnerablility
data, match the CVE to a database automatically gathered in a SQL DB server. Triage the
vulnerability with an algorithm we create that gives a score that goes more in depth than the
normal CVSS score then allow the user to automatically patch 1-2 vulnerabilities through a
dialog box or Command-line input. Coding language will be python with powershell for
windows or bash for linux.
Prefer Linux.
Vulnerability scanner. open vas / Nessus (free version)/ any scanner with edu license.
Maybe use open vas automated scanning. when scanning it will give possible vulnerabilities of a
system (need multiple vulnerable vms). Periodically.
Damn vulnerable web app.
Gathering a report with which vulnerabilities exist on each computer. Any format xml whatever.
Output given from scanner.
Need to parse to grab cve # for match in sql database.
Reading this vulnerability and checking possible solutions from CVE list.
https://capec.mitre.org/ → Create DB in SQL
https://cve.mitre.org/ → Create DB in SQL
Notes: Doesn’t need to be the full database can just be 10-12 cve’s we manually input.
Triage Vulnerabilities Automatically with python algorithm.
Exploit existence / maturity will be taken into account which dives deeper into a v
vulnerability than the cvss score
If there are any mitigations. 1 or 2 semi automatic solutions applied.
Powershell Maybe.
Example we find one vulnerability

from crontab import CronTab
import os

#access the system crontab of the current user
user_cron = CronTab(user=os.getlogin())

#Lists current cron jobs
print("List of current cron jobs:")
for job in user_cron:
    print(job)

#Clears all current cron jobs
clear_jobs = input("Do you wish to clear jobs? (Y/N): ")
if(clear_jobs == 'Y'):
    user_cron.remove_all()
    user_cron.write()

#Creates new cron job that'll start the scanning script
scan_job = user_cron.new(command='python ./gvm-scripts/create-and-scan-host-all-in-one.py')

print("This program will ask for a day of the week, hour, and minute to start the automatic scanning")
print("The vulnurability fixes will be automatically set to run an hour after the scan")

_exit = input("Do you wish to continute with scan scheduling? (Y/N): ")
if(_exit == 'Y'):

    #Prompts for day, hour, and minute to schedule the job
    day_of_week = int(input("Enter number 0-6 for desired weekday to run scan (where 0 is Sunday): "))
    scan_job.dow.on(day_of_week)

    set_hour = int(input("Enter hour (0-23): "))
    scan_job.hour.on(set_hour)

    set_minute = int(input("Enter minutes: "))
    scan_job.minute.on(set_minute)

    #Main script will be set 1 hour after user input
    main_job = user_cron.new(command='python ./main.py')

    main_job.dow.on(day_of_week)
    main_job.hour.on(set_hour+1)
    main_job.minute.on(set_minute)
    user_cron.write()   #Writes the job to the crontab
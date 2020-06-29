# module to run worker using cron every 15 minutes


import notificationHandler
import os
import subprocess
from crontab import CronTab

user = "cinnamon"

def getCommandDirectory():
    #rstrip to remove trailing newline, decode to convert string to bytes using utf-8 encoding
    python3Directory = subprocess.check_output(["which","python3"]).rstrip().decode("utf-8") 
    workingDirectory = os.getcwd()
    appName = "/notificationHandler.py"
    commandDirectory = python3Directory + " " + workingDirectory + appName
    return commandDirectory

def runWorkerAsCronJob():
    try:
        cron = CronTab(user=user)
        job = cron.new(command=getCommandDirectory()) 
        # run every 15 minutes
        job.minutes.every(15)
        cron.write()
        print("Cron job has been written")
    except:
        print("Unable to write cron job")

runWorkerAsCronJob()
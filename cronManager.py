# module to run worker using cron every 15 minutes

import os
import subprocess
from crontab import CronTab

def getCommandDirectory(directory):
    #rstrip to remove trailing newline, decode to convert bytes to string using utf-8 encoding
    python3Directory = subprocess.check_output(["which","python3"]).rstrip().decode("utf-8") 
    rootDirectory = os.getcwd()
    appName = directory
    commandDirectory = python3Directory + " " + rootDirectory + appName
    return commandDirectory

def runWorkerAsCronJob(user, directory, minutes):
    try:
        cron = CronTab(user=user)
        job = cron.new(command=getCommandDirectory(directory)) 
        # run every 15 minutes
        job.minutes.every(minutes)
        cron.write()
        print("Cron job has been written at " + directory + " with user " + user)
    except:
        print("Unable to write cron job")
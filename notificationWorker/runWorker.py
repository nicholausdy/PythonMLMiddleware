import sys
sys.path.append("..")
import cronManager

user = "cinnamon"
directory = "/notificationHandler.py"
minutes = 1
cronManager.runWorkerAsCronJob(user, directory, minutes)
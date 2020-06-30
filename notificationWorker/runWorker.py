import sys
sys.path.append("..")
import cronManager

import os
from pathlib import Path
from dotenv import load_dotenv
env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)

user = os.getenv("CRON_USER")
directory = "/notificationHandler.py"
minutes = 15
cronManager.runWorkerAsCronJob(user, directory, minutes)
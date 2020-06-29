import natsPublish
import os
import subprocess
#timestamp = 23000999
#data = {'timestamp': timestamp}

#natsPublish.runPublisher(data)
currentDirectory = os.getcwd()
#rstrip to remove trailing newline, decode to convert string to bytes using utf-8 encoding
s = subprocess.check_output(["which","python3"]).rstrip().decode("utf-8") 
commandDirectory = s + " " + currentDirectory
print(commandDirectory)

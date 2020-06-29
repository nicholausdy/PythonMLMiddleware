import natsPublish

# fetch latest timestamp from database
def getTimeStamp():
    timestamp = 23000999
    data = {'timestamp': timestamp}
    return data

# run worker once:
natsPublish.runPublisher(getTimeStamp())
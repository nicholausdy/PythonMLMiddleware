import natsPublish

timestamp = 23000999
data = {'timestamp': timestamp}

natsPublish.notificationHandler(data)
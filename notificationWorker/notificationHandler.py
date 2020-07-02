import natsPublish

# call stored procedure from DB to fetch input data for prediction
## def getPredictionInputData() // can be run as separate service / API, py file stored on predictionWorker

# call predict function, store prediction result on DB
## def predictData(): // can be run as separate service / API, py file stored on predictionWorker

# fetch latest timestamp from database to show latest prediction data
def getTimeStamp():
    timestamp = 23000999
    data = {'timestamp': timestamp}
    return data

# run worker once:
## getPredictionInputData() // 
## predictData()
natsPublish.runPublisher(getTimeStamp())
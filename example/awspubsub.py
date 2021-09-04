import time as t
import json
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT

# Define ENDPOINT, CLIENT_ID, PATH_TO_CERT, PATH_TO_KEY, PATH_TO_ROOT, MESSAGE, TOPIC, and RANGE
ENDPOINT = "xxxx"
CLIENT_ID = "12345"
PATH_TO_CERT = "./name-certificate.pem.crt"
PATH_TO_KEY = "./name-private.pem.key"
PATH_TO_ROOT = "./name.pem"

myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
myAWSIoTMQTTClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)

def publish(id, data):   
    topic = 'something/' + id 
    message = {"message" : data}
    myAWSIoTMQTTClient.publish(topic, json.dumps(message), 1) 

def subscribe():      
    myAWSIoTMQTTClient.subscribe('something/#', 1, customCallback)

def customCallback(client, userdata, message):
    topic = (message.topic)
    receivedMessage = json.loads((message.payload).decode('unicode_escape'))
    message = receivedMessage['message']
    print ('topic:', topic )
    print ('message:', message)

myAWSIoTMQTTClient.connect(1200)
subscribe()

while (True):
    print('publishing...')
    publish('12345', 'teste pub-sub')
    t.sleep(3)
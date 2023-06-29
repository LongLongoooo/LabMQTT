import sys
import random
import time
from Adafruit_IO import MQTTClient
import requests

AIO_USERNAME = "PhamBaoLongGroupAI"
AIO_KEY = ""
global_equation = "(x1*x2)/x3" #global variable

def init_global_equation(): #Implement the HTTP Get
    headers = {}
    aio_url = ""
    x = requests.get(url = aio_url, headers = headers, verify = False)
    data = x.json()
    global_equation = data["last_value"]
    print("Get lastest value:", global_equation)
    
def modify_value(x1, x2, x3): #Eval_funciton
    result = eval(global_equation)
    print(result)
    return result

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe successfully ...")
    
def connected(client):
    print("Connect successfully ...")
    client.subscribe("button1")
    client.subscribe("equation")

def disconnected(client):
    print("Disconnect ...")
    sys.exit (1)


def message(client , feed_id , payload):
    print("Input data: " + payload)
    if (feed_id == "equation"):
        global_equation = payload
        print(global_equation)
        
client = MQTTClient(AIO_USERNAME , AIO_KEY)
    
client.on_connect = connected #function pointer
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe

client.connect()
client.loop_background()
init_global_equation()

while True:
    time.sleep(3)
    sensor1 = random.randint(20, 100)
    sensor2 = random.randint(50, 200)
    sensor3 = random.randint(12, 49)
    client.publish("sensor1", sensor1)
    client.publish("sensor2", sensor2) 
    client.publish("sensor3", sensor3)
    sensor4 = modify_value(sensor1, sensor2, sensor3)
    print("sensor1: ", sensor1)
    print("sensor2: ", sensor2)
    print("sensor3: ", sensor3)
    print("Result: ", sensor4)
    break
    pass


import sys
import random
import time
from Adafruit_IO import MQTTClient
AIO_USERNAME = "PhamBaoLongGroupAI"
AIO_KEY = "aio_QQwL63yQXkZFqCKB3yvPEDdpFod0"
def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")
    
def connected(client):
    print("Ket noi thanh cong ...")
    client.subscribe("button1")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)

client = MQTTClient(AIO_USERNAME , AIO_KEY)

client.on_connect = connected #function pointer
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe

client.connect()
client.loop_background()

while True:
    time.sleep(5)
    client.publish("sensor1", random.randint(20, 700))
    pass

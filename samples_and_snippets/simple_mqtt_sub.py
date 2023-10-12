import paho.mqtt.client as paho

from paho.mqtt.client import MQTTMessage
import time

BROKER, PORT = "localhost", 1883

def on_message(client, userdata, msg):
    print(f'Received {msg.payload.decode()}')


def pressed():
    while True:
        radomnumber = 7
        client.publish("pressbutton", radomnumber)
        print("Just publisj ranodm to topic presss")
        time.sleep(1)
        
 

client = paho.Client()
client.on_message = on_message
client.connect(BROKER, PORT)
client.subscribe("lot/sensor")
pressed()

client.loop_forever()

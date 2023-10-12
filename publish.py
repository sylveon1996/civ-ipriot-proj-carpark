import time

import paho.mqtt.client as paho

broker = 'localhost'
port = 1883
 
client = paho.Client()

client.connect(broker, port)


from sense_emu import SenseHat

sense = SenseHat()



worddesu = "Pokemon"


while True:
  for event in sense.stick.get_events():
    
    if event.action == "pressed":
      #sense.show_message("Press button", text_colour=[255, 0, 0])
      entry = "this is data data"
      client.publish('test',  entry )
      


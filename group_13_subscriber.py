#Ali Khaleel
#Abdulkadir Musse
#Abel Teklemariam

import paho.mqtt.client as mqtt
import json

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

class Subscriber:
    def __init__(self, topic='COMP216'):
        self.client = mqtt.Client()
        self.topic = topic

    def subscribe(self):

        #Generate a client
        self.client.on_message = on_message

        self.client.connect('localhost', 1883)

        self.client.subscribe(self.topic)

        print(f"Subscribed to topic '{self.topic}'")

        self.client.loop_forever()

sub = Subscriber()
sub.subscribe()

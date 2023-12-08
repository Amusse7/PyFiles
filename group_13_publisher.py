#Ali Khaleel
#Abdulkadir Musse
#Abel Teklemariam

import paho.mqtt.client as mqtt
from time import sleep
from util import create_data 

class Publisher:
    def __init__(self, delay=0.75, topic='COMP216'):
        self.client = mqtt.Client()
        self.topic = topic
        self.delay = delay

    def publish(self, times=1):
        self.client.connect('localhost', 1883)  
        for x in range(times):
            print(f'#{x}', end=' ')
            self.__publish()
            sleep(self.delay) 

        self.client.disconnect()  

    def __publish(self):
        data = create_data()  
        print(f'{data} to broker')  
        self.client.publish(self.topic, payload=str(data))  

pub = Publisher()
pub.publish(10)

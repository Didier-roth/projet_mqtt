from mqtt.Mqtt import Mqtt
import random
class Producteur(Mqtt):
    MessageCounter = 0
    def __init__(self, brokerIP, brokerPort):
        super().__init__(brokerIP, brokerPort)

    def getMessagesCounter(self):
        return self.MessageCounter

    def publish(self, topic, message, counter=False, qos=1):
        if self.MessageCounter == 0:
            self.MessageCounter = 1
        if counter:
            toSend = str(self.MessageCounter) + " : " + message
            self.client.publish(topic, toSend, qos)
        else:
            self.client.publish(topic, message, qos)
        self.MessageCounter += 1


    def publishMessages(self, topic, nbMessages, counter=False, qos=1):
        for i in range(nbMessages):
            message = self.generateMessage(15)
            if counter:
                self.publish(topic, message, counter, qos)
            else:
                self.publish(topic, message, counter, qos)
            i=+1

    @staticmethod
    def generateMessage(size=10):
        mot = ""
        caracteres = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789"
        for i in range(size):
            lettre = caracteres[random.randint(0, len(caracteres) - 1)]
            mot += lettre
            i=+1
        return mot




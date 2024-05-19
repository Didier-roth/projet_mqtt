from mqtt import Mqtt, Producteur

#Mqtt.Mqtt("192.168.0.19", 1883)
prod = Producteur.Producteur("192.168.0.19", 1883)
prod.identify("pi","raspberry")
prod.connect()
prod.publish("topic", "message",False,0)
prod.publishMessages("topic", 20, True)


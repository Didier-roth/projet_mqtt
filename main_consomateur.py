from mqtt import Mqtt, Consomateur

def onMessage(client, userdata, message):
    print("Message received: " + str(message.payload.decode("utf-8")))

def onLog(client, userdata, level, buf):
    print("log: " + str(level) + " - " + buf)

def onLogFile(client, userdata, level, buf):
    f = open(
        'C:\\Users\\didie\\OneDrive - Enseignement de la Province de Liège\\cours\\ISIL\\2023 - 2024\\Q2\\SmartCities\\Wilvers\\projet_mqtt\\log.txt',
        "a")
    f.write("log: " + str(level) + " - " + buf)
    f.close()

def onTopicMessage(client, userdata, message):
    print("Message received on topic message: " + str(message.payload.decode("utf-8")))

cons = Consomateur.Consomateur("192.168.0.19", 1883)
cons.identify("pi","raspberry")
cons.connect()
cons.setOnLog(onLog)
cons.souscrire("topic")
cons.souscrire("message")
cons.setDefaultCallback(onMessage)
cons.setCallback("message", onTopicMessage)
cons.loopForever()


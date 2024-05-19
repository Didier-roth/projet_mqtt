import os
from pathlib import Path

from appdata import AppDataPaths

from mqtt.Mqtt import Mqtt
import random
class Consomateur(Mqtt):
    topics = []
    def __init__(self, brokerIP, brokerPort):
        super().__init__(brokerIP, brokerPort)
        app_paths = AppDataPaths()
        self.logDir = app_paths.logs_path
        Path(self.logDir).mkdir(parents=True, exist_ok=True)

    def defaultOnLog(self, client, level, buf):
        f = open(os.path.join(self.logDir, "log.txt"), "a")
        f.write("log: " + str(level) + " - " + buf)
        f.close()
    def souscrire(self, topic):
        if topic not in self.topics:
            self.client.subscribe(topic)
            self.topics.append(topic)

    def desouscrire(self, topic):
        if topic in self.topics:
            self.client.unsubscribe(topic)
            self.topics.remove(topic)

    def setDefaultCallback(self, func):
        self.client.on_message = func

    def setCallback(self,topic,func):
        self.client.message_callback_add(topic, func)

    def start(self):
        self.client.loop_start()

    def stop(self):
        self.client.loop_stop()

    def loopForever(self):
        self.client.loop_forever()

    def getTopics(self):
        return self.topics

    def setOnLog(self, func):
        self.client.on_log = func





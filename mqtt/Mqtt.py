import paho.mqtt.client
class Mqtt:
    def __init__(self, ip, port):
        self.Username = None
        self.Password = None
        self.Ip = ip
        self.Port = port
        self.client = paho.mqtt.client.Client()

    def identify(self, user, pwd):
        self.Username = user
        self.Password = pwd

    def connect(self):
        print("Connecting to broker")
        if self.Username is not None:
            self.client.username_pw_set(self.Username, self.Password)
        self.client.connect(self.Ip, self.Port)
        print("Connected to broker")

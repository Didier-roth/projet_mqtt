import os
import sys
from pathlib import Path

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMainWindow
from appdata import AppDataPaths


import connexionWindow
import mqttWindow
from mqtt import Producteur, Consomateur
class MainWindow(QMainWindow):
    # Constructor
    def __init__(self):
        self.Cons = None
        self.Prod = None
        super().__init__()
        self.setupUI()

        self.login = connexionWindow.connexionWindow()
        self.login.setDefaultValue("127.0.0.1","1883","pi","raspberry")

        if self.login.exec():
            print("ok")
            broker = self.login.LineBroker.text()
            port = self.login.LinePort.text()
            if self.login.checkBoxAuthenticate.isChecked():
                user = self.login.LineUser.text()
                pwd = self.login.LinePwd.text()
                self.connect(broker,port,user,pwd)
            else :
                self.connect(broker,port)
        else:
            sys.exit()

        app_paths = AppDataPaths()
        self.logDir = app_paths.logs_path
        Path(self.logDir).mkdir(parents=True, exist_ok=True)
        print(self.logDir)
        f = open(os.path.join(self.logDir, "log.txt"), "w")
        f.write("log: " + " - " + "Start"+"\n")
        f.close()




    def connect(self,broker,port,user = None,pwd = None):
        print(broker, port)
        self.Prod = Producteur.Producteur(broker, int(port))
        if user is not None:
            self.Prod.identify(user,pwd)
        self.Prod.connect()
        self.Cons = Consomateur.Consomateur(broker, int(port))
        if user is not None:
            self.Cons.identify(user,pwd)
        self.Cons.connect()
        self.Cons.setDefaultCallback(self.onMessage)
        self.Cons.setOnLog(self.onLog)
        self.Cons.start()


    def onMessage(self,client, userdata, message):
        print("Message received: " + str(message.payload.decode("utf-8)") + " on topic: " + message.topic))
        self.listMessages.addItem("Topic : " + message.topic + " -> " + message.payload.decode("utf-8)"))

    def onLog(self,client, userdata, level, buf):
        f = open(os.path.join(self.logDir, "log.txt"), "a")
        f.write("log: " + str(level) + " - " + buf+"\n")
        f.close()


    def setupUI(self):
        font = QFont()
        font.setPointSize(20)
        self.labelTopic = QtWidgets.QLabel()
        self.labelTopic.setFont(font)

        self.LineTopic = QtWidgets.QLineEdit()

        self.buttonAdd = QtWidgets.QPushButton()

        self.buttonDel  = QtWidgets.QPushButton()

        self.listTopics = QtWidgets.QListWidget()

        self.labelTopicMessage = QtWidgets.QLabel()

        self.listMessages = QtWidgets.QListWidget()

        self.labelMessage = QtWidgets.QLabel()

        self.lineMessage = QtWidgets.QLineEdit()

        self.lineTopic = QtWidgets.QLineEdit()

        self.buttonSend = QtWidgets.QPushButton()

        self.buttonClear = QtWidgets.QPushButton()

        self.layoutVTopic = QtWidgets.QVBoxLayout()
        self.layoutVTopic.addWidget(self.labelTopic,alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layoutVTopic.addWidget(self.LineTopic)
        self.layoutHAddDel = QtWidgets.QHBoxLayout()
        self.layoutHAddDel.addWidget(self.buttonAdd)
        self.layoutHAddDel.addWidget(self.buttonDel)
        self.layoutVTopic.addLayout(self.layoutHAddDel)
        self.layoutVTopic.addWidget(self.listTopics)

        self.layoutVMessage = QtWidgets.QVBoxLayout()
        self.layoutVMessage.addWidget(self.listMessages)
        self.layoutVMessage.addWidget(self.labelMessage)
        self.layoutVMessage.addWidget(self.lineMessage)
        self.layoutVMessage.addWidget(self.labelTopicMessage)
        self.layoutVMessage.addWidget(self.lineTopic)

        self.layoutHSendClear = QtWidgets.QHBoxLayout()
        self.layoutHSendClear.addWidget(self.buttonSend)
        self.layoutHSendClear.addWidget(self.buttonClear)

        self.layoutVMessage.addLayout(self.layoutHSendClear)


        self.layoutH = QtWidgets.QHBoxLayout()
        self.layoutH.addLayout(self.layoutVTopic)
        self.layoutH.addLayout(self.layoutVMessage)

        self.setCentralWidget(QtWidgets.QWidget())
        self.centralWidget().setLayout(self.layoutH)

        self.buttonSend.clicked.connect(self.sendMessage)
        self.buttonAdd.clicked.connect(self.addTopic)
        self.buttonClear.clicked.connect(self.clearMessages)
        self.buttonDel.clicked.connect(self.delTopic)

        self.retranslateUi()

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Dialog", u"Client", None))
        self.labelTopic.setText(QCoreApplication.translate("Dialog", u"Topics", None))
        self.buttonAdd.setText(QCoreApplication.translate("Dialog", u"ADD", None))
        self.buttonSend.setText(QCoreApplication.translate("Dialog", u"SEND", None))
        self.buttonClear.setText(QCoreApplication.translate("Dialog", u"CLEAR", None))
        self.labelMessage.setText(QCoreApplication.translate("Dialog", u"Messages", None))
        self.labelTopicMessage.setText(QCoreApplication.translate("Dialog", u"Topic", None))
        self.buttonDel.setText(QCoreApplication.translate("Dialog", u"DEL", None))
        # retranslateUi

    def addTopic(self):
        topic = self.LineTopic.text()
        if topic == "":
            return
        if self.Cons is not None:
            self.Cons.souscrire(topic)
            self.listTopics.addItem(topic)
            self.LineTopic.clear()

    def delTopic(self):
        item = self.listTopics.takeItem(self.listTopics.currentRow())
        topic = item.text()
        if self.Cons is not None:
            self.Cons.desouscrire(topic)
        self.listTopics.removeItemWidget(item)

    def sendMessage(self):
        message = self.lineMessage.text()
        topic = self.lineTopic.text()
        if topic == "" or message == "":
            return
        if self.Prod is not None:
            self.Prod.publish(topic,message)
            self.lineMessage.clear()
            self.lineTopic.clear()

    def closeEvent(self, event):
        if self.Cons is not None:
            self.Cons.stop()
        event.accept()

    def clearMessages(self):
        self.listMessages.clear()
        self.lineMessage.clear()
        self.lineTopic.clear()




app = QtWidgets.QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec_()
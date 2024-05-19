# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connexion.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
                               QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget, QDialogButtonBox, QCheckBox)

class connexionWindow(QDialog):

    def __init__(self):
        super().__init__()

        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        self.labelConnexion = QLabel()
        self.labelConnexion.setFont(font)

        self.labelBroker = QLabel()
        self.LineBroker = QLineEdit()

        self.labelPort = QLabel()
        self.LinePort = QLineEdit()


        self.labelAuthenticate = QLabel()
        self.labelAuthenticate.setFont(font)

        self.checkBoxAuthenticate = QCheckBox()


        self.labelUser = QLabel()
        self.LineUser = QLineEdit()

        self.labelPwd = QLabel()
        self.LinePwd = QLineEdit()

        qBtn = QDialogButtonBox.Ok | QDialogButtonBox.Close
        self.buttonConnect = QDialogButtonBox(qBtn)
        self.buttonConnect.accepted.connect(self.accept)
        self.buttonConnect.rejected.connect(self.reject)


        self.layout = QVBoxLayout()
        self.layout.addWidget(self.labelConnexion,alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.labelBroker)
        self.layout.addWidget(self.LineBroker)
        self.layout.addWidget(self.labelPort)
        self.layout.addWidget(self.LinePort)
        self.layout.addWidget(self.labelAuthenticate,alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.checkBoxAuthenticate)
        self.layout.addWidget(self.labelUser)
        self.layout.addWidget(self.LineUser)
        self.layout.addWidget(self.labelPwd)
        self.layout.addWidget(self.LinePwd)
        self.layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.layout.addWidget(self.buttonConnect,alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.layout)
        self.checkBoxAuthenticate.stateChanged.connect(self.onStateChanged)
        self.checkBoxAuthenticate.setChecked(False)
        self.disableAuthenticate()

        self.retranslateUi()

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Dialog", u"Connexion", None))
        self.labelConnexion.setText(QCoreApplication.translate("Dialog", u"Connexion", None))
        self.labelBroker.setText(QCoreApplication.translate("Dialog", u"IP BROKER", None))
        self.labelPort.setText(QCoreApplication.translate("Dialog", u"PORT", None))
        self.labelUser.setText(QCoreApplication.translate("Dialog", u"User", None))
        self.labelPwd.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.labelAuthenticate.setText(QCoreApplication.translate("Dialog", u"Authentication", None))
        self.checkBoxAuthenticate.setText(QCoreApplication.translate("Dialog", u"Use Credentials ?", None))
        # retranslateUi

    def setDefaultValue(self, ip, port, user, pwd):
        self.LineBroker.setText(ip)
        self.LinePort.setText(port)
        self.LineUser.setText(user)
        self.LinePwd.setText(pwd)

    def onStateChanged(self):
        if self.checkBoxAuthenticate.isChecked():
            self.enableAuthenticate()
        else:
            self.disableAuthenticate()

    def enableAuthenticate(self):
        self.labelUser.setEnabled(True)
        self.labelPwd.setEnabled(True)
        self.LineUser.setEnabled(True)
        self.LinePwd.setEnabled(True)

    def disableAuthenticate(self):
        self.labelUser.setEnabled(False)
        self.labelPwd.setEnabled(False)
        self.LineUser.setEnabled(False)
        self.LinePwd.setEnabled(False)


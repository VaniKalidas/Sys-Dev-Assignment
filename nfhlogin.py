# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nfhlogin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(400, 300)
        Login.setMinimumSize(QtCore.QSize(400, 300))
        self.usrbox = QtWidgets.QLineEdit(Login)
        self.usrbox.setGeometry(QtCore.QRect(170, 120, 181, 31))
        self.usrbox.setObjectName("usrbox")
        self.passbox = QtWidgets.QLineEdit(Login)
        self.passbox.setGeometry(QtCore.QRect(170, 180, 181, 31))
        self.passbox.setText("")
        self.passbox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passbox.setObjectName("passbox")
        self.nfhlbl = QtWidgets.QLabel(Login)
        self.nfhlbl.setGeometry(QtCore.QRect(50, 40, 301, 41))
        self.nfhlbl.setObjectName("nfhlbl")
        self.usrlbl = QtWidgets.QLabel(Login)
        self.usrlbl.setGeometry(QtCore.QRect(50, 120, 91, 21))
        self.usrlbl.setObjectName("usrlbl")
        self.passlbl = QtWidgets.QLabel(Login)
        self.passlbl.setGeometry(QtCore.QRect(50, 180, 91, 21))
        self.passlbl.setObjectName("passlbl")
        self.OKbtn = QtWidgets.QPushButton(Login)
        self.OKbtn.setGeometry(QtCore.QRect(170, 240, 81, 31))
        self.OKbtn.setObjectName("OKbtn")
        self.pushButton_2 = QtWidgets.QPushButton(Login)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 240, 81, 31))
        self.pushButton_2.setObjectName("Cnlbtn")

        self.retranslateUi(Login)
        self.pushButton_2.clicked.connect(Login.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.nfhlbl.setText(_translate("Login", "<html><head/><body><p><span style=\" font-size:26pt;\">Nympton Food Hub</span></p></body></html>"))
        self.usrlbl.setText(_translate("Login", "<html><head/><body><p><span style=\" font-size:12pt;\">Username:</span></p></body></html>"))
        self.passlbl.setText(_translate("Login", "<html><head/><body><p><span style=\" font-size:12pt;\">Password:</span></p></body></html>"))
        self.OKbtn.setText(_translate("Login", "OK"))
        self.pushButton_2.setText(_translate("Login", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
# Form implementation generated from reading ui file 'alert2.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_alert2(object):
    def setupUi(self, alert2):
        alert2.setObjectName("alert2")
        alert2.resize(210, 84)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("clock.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        alert2.setWindowIcon(icon)
        alert2.setStyleSheet("QDialog {\n"
"background-color:black;\n"
"}")
        self.buttonBox = QtWidgets.QDialogButtonBox(alert2)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.remi = QtWidgets.QLineEdit(alert2)
        self.remi.setGeometry(QtCore.QRect(10, 10, 191, 31))
        self.remi.setStyleSheet("QLineEdit {\n"
"\n"
"border-radius:5px;\n"
"background-color:rgb(240, 240, 241)\n"
"\n"
"}")
        self.remi.setText("")
        self.remi.setObjectName("remi")
        self.pushButt = QtWidgets.QPushButton(alert2)
        self.pushButt.setGeometry(QtCore.QRect(60, 50, 93, 28))
        self.pushButt.setStyleSheet("QPushButton{\n"
"border-radius:5px;\n"
"background-color:rgb(240, 240, 241)\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(0, 244, 138);\n"
"font-size: 20px\n"
"}\n"
"")
        self.pushButt.setObjectName("pushButt")

        self.retranslateUi(alert2)
        self.buttonBox.accepted.connect(alert2.accept) # type: ignore
        self.buttonBox.rejected.connect(alert2.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(alert2)

    def retranslateUi(self, alert2):
        _translate = QtCore.QCoreApplication.translate
        alert2.setWindowTitle(_translate("alert2", "Alert"))
        self.pushButt.setText(_translate("alert2", "OK"))


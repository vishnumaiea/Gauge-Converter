# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AWG-SWG.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GaugeToolBox(object):
    def setupUi(self, GaugeToolBox):
        GaugeToolBox.setObjectName(_fromUtf8("GaugeToolBox"))
        GaugeToolBox.resize(805, 503)
        GaugeToolBox.setMinimumSize(QtCore.QSize(805, 503))
        GaugeToolBox.setMaximumSize(QtCore.QSize(805, 503))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("8514oem"))
        GaugeToolBox.setFont(font)
        self.comboBox = QtGui.QComboBox(GaugeToolBox)
        self.comboBox.setGeometry(QtCore.QRect(40, 110, 191, 51))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.line = QtGui.QFrame(GaugeToolBox)
        self.line.setGeometry(QtCore.QRect(260, 60, 20, 431))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.lineEdit = QtGui.QLineEdit(GaugeToolBox)
        self.lineEdit.setGeometry(QtCore.QRect(40, 220, 191, 51))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(GaugeToolBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 330, 191, 51))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(GaugeToolBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 330, 191, 51))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(GaugeToolBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(310, 220, 191, 51))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.line_2 = QtGui.QFrame(GaugeToolBox)
        self.line_2.setGeometry(QtCore.QRect(530, 60, 20, 431))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.comboBox_2 = QtGui.QComboBox(GaugeToolBox)
        self.comboBox_2.setGeometry(QtCore.QRect(310, 110, 191, 51))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.lineEdit_5 = QtGui.QLineEdit(GaugeToolBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(580, 330, 191, 51))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(GaugeToolBox)
        self.lineEdit_6.setGeometry(QtCore.QRect(580, 220, 191, 51))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.comboBox_3 = QtGui.QComboBox(GaugeToolBox)
        self.comboBox_3.setGeometry(QtCore.QRect(580, 110, 191, 51))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.label = QtGui.QLabel(GaugeToolBox)
        self.label.setGeometry(QtCore.QRect(40, 290, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(GaugeToolBox)
        self.label_2.setGeometry(QtCore.QRect(40, 180, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(GaugeToolBox)
        self.label_3.setGeometry(QtCore.QRect(310, 180, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(GaugeToolBox)
        self.label_4.setGeometry(QtCore.QRect(310, 290, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(GaugeToolBox)
        self.label_5.setGeometry(QtCore.QRect(580, 180, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(GaugeToolBox)
        self.label_6.setGeometry(QtCore.QRect(580, 290, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton = QtGui.QPushButton(GaugeToolBox)
        self.pushButton.setGeometry(QtCore.QRect(40, 430, 191, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(GaugeToolBox)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 430, 191, 51))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(GaugeToolBox)
        self.pushButton_3.setGeometry(QtCore.QRect(580, 430, 191, 51))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_7 = QtGui.QLabel(GaugeToolBox)
        self.label_7.setGeometry(QtCore.QRect(40, 70, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(GaugeToolBox)
        self.label_8.setGeometry(QtCore.QRect(310, 70, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(GaugeToolBox)
        self.label_9.setGeometry(QtCore.QRect(580, 70, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.retranslateUi(GaugeToolBox)
        QtCore.QMetaObject.connectSlotsByName(GaugeToolBox)

    def retranslateUi(self, GaugeToolBox):
        GaugeToolBox.setWindowTitle(_translate("GaugeToolBox", "Gauge Converter", None))
        self.label.setText(_translate("GaugeToolBox", "SWG", None))
        self.label_2.setText(_translate("GaugeToolBox", "AWG", None))
        self.label_3.setText(_translate("GaugeToolBox", "Gauge", None))
        self.label_4.setText(_translate("GaugeToolBox", "SWG", None))
        self.label_5.setText(_translate("GaugeToolBox", "Gauge", None))
        self.label_6.setText(_translate("GaugeToolBox", "AWG", None))
        self.pushButton.setText(_translate("GaugeToolBox", "Reset", None))
        self.pushButton_2.setText(_translate("GaugeToolBox", "Reset", None))
        self.pushButton_3.setText(_translate("GaugeToolBox", "Reset", None))
        self.label_7.setText(_translate("GaugeToolBox", "Gauge", None))
        self.label_8.setText(_translate("GaugeToolBox", "AWG", None))
        self.label_9.setText(_translate("GaugeToolBox", "SWG", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    GaugeToolBox = QtGui.QDialog()
    ui = Ui_GaugeToolBox()
    ui.setupUi(GaugeToolBox)
    GaugeToolBox.show()
    sys.exit(app.exec_())


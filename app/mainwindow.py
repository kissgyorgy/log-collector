# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Oct 23 19:01:14 2014
#      by: PyQt4 UI code generator 4.11.1
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(349, 207)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayout = QtGui.QFormLayout(self.centralwidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setContentsMargins(12, 12, 12, -1)
        self.formLayout.setVerticalSpacing(5)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_5)
        self.url = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.url.sizePolicy().hasHeightForWidth())
        self.url.setSizePolicy(sizePolicy)
        self.url.setMinimumSize(QtCore.QSize(200, 0))
        self.url.setCursorPosition(0)
        self.url.setObjectName(_fromUtf8("url"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.url)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.timestamp = QtGui.QDateTimeEdit(self.centralwidget)
        self.timestamp.setCalendarPopup(True)
        self.timestamp.setObjectName(_fromUtf8("timestamp"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.timestamp)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.dim1 = QtGui.QSpinBox(self.centralwidget)
        self.dim1.setObjectName(_fromUtf8("dim1"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.dim1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.dim2 = QtGui.QSpinBox(self.centralwidget)
        self.dim2.setObjectName(_fromUtf8("dim2"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.dim2)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_4)
        self.value = QtGui.QDoubleSpinBox(self.centralwidget)
        self.value.setMinimumSize(QtCore.QSize(100, 0))
        self.value.setMaximum(999999999.0)
        self.value.setObjectName(_fromUtf8("value"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.value)
        self.send = QtGui.QPushButton(self.centralwidget)
        self.send.setObjectName(_fromUtf8("send"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.send)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_5.setText(_translate("MainWindow", "Szerver URL:", None))
        self.url.setText(_translate("MainWindow", "http://127.0.0.1:5000/new", None))
        self.label.setText(_translate("MainWindow", "timestamp", None))
        self.label_2.setText(_translate("MainWindow", "dim1", None))
        self.label_3.setText(_translate("MainWindow", "dim2", None))
        self.label_4.setText(_translate("MainWindow", "value", None))
        self.send.setText(_translate("MainWindow", "Küldés!", None))


#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#~ Copyright (C) 2014 Carlos Manuel Ferras Hernandez
#~ This file is part of LF02_package.

#~ LF02_package is free software: you can redistribute it and/or modify
#~ it under the terms of the GNU General Public License as published by
#~ the Free Software Foundation, either version 3 of the License, or
#~ (at your option) any later version.

#~ LF02_package is distributed in the hope that it will be useful,
#~ but WITHOUT ANY WARRANTY; without even the implied warranty of
#~ MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#~ GNU General Public License for more details.

#~ You should have received a copy of the GNU General Public License
#~ along with LF02_package.  If not, see <http://www.gnu.org/licenses/>.
from PyQt4 import QtCore, QtGui
from style import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        widget=QtGui.QDesktopWidget()
	mainScreenSize = widget.availableGeometry(widget.primaryScreen())
	x= mainScreenSize.width()/2-371
	y= mainScreenSize.height()/2-120
	Dialog.setGeometry(QtCore.QRect(x, y, 743, 241))
        Dialog.setMinimumSize(QtCore.QSize(743, 241))
        Dialog.setMaximumSize(QtCore.QSize(743, 241))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(6, 10, 638, 221))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
	self.frame.setStyleSheet(PROCESS_WIN_STYLE)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(210, 124, 151, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.spinBox = QtGui.QSpinBox(self.frame)
        self.spinBox.setGeometry(QtCore.QRect(332, 120, 54, 27))
        self.spinBox.setMaximum(512)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox_2 = QtGui.QSpinBox(self.frame)
        self.spinBox_2.setGeometry(QtCore.QRect(130, 120, 54, 27))
        self.spinBox_2.setMaximum(512)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(10, 124, 121, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.spinBox_3 = QtGui.QSpinBox(self.frame)
        self.spinBox_3.setGeometry(QtCore.QRect(520, 120, 54, 27))
        self.spinBox_3.setMaximum(512)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.label_9 = QtGui.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(410, 124, 121, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.line_2 = QtGui.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(10, 50, 623, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(10, 150, 623, 21))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_10 = QtGui.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 121, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.comboBox = QtGui.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(95, 16, 61, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label_12 = QtGui.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(180, 20, 131, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.spinBox_5 = QtGui.QSpinBox(self.frame)
        self.spinBox_5.setGeometry(QtCore.QRect(300, 16, 54, 27))
        self.spinBox_5.setMaximum(100)
        self.spinBox_5.setObjectName(_fromUtf8("spinBox_5"))	
        self.label_14 = QtGui.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(10, 70, 61, 17))
        self.label_14.setObjectName(_fromUtf8("label_14"))	
	self.label_15 = QtGui.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(78, 70, 41, 17))
        self.label_15.setObjectName(_fromUtf8("label_14"))	
	self.label_16 = QtGui.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(125, 70, 111, 17))
        self.label_16.setObjectName(_fromUtf8("label_14"))	
	self.label_17 = QtGui.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(230, 70, 51, 17))
        self.label_17.setObjectName(_fromUtf8("label_14"))	
        self.spinBox_6 = QtGui.QSpinBox(self.frame)
        self.spinBox_6.setGeometry(QtCore.QRect(400, 65, 54, 27))
        self.spinBox_6.setMaximum(100)
        self.spinBox_6.setObjectName(_fromUtf8("spinBox_6"))
        self.label_13 = QtGui.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(295, 70, 111, 17))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 171, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.frame)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(155, 176, 62, 27))
        self.doubleSpinBox_2.setMaximum(600.0)
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(245, 180, 131, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.frame)
        self.doubleSpinBox.setGeometry(QtCore.QRect(370, 176, 61, 27))
        self.doubleSpinBox.setMinimum(0.1)
        self.doubleSpinBox.setMaximum(20.0)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(460, 180, 120, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.doubleSpinBox_3 = QtGui.QDoubleSpinBox(self.frame)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(563, 176, 62, 27))
        self.doubleSpinBox_3.setMaximum(999999999.0)
        self.doubleSpinBox_3.setObjectName(_fromUtf8("doubleSpinBox_3"))
        self.pushButton = QtGui.QPushButton(Dialog)
	self.pushButton.setStyleSheet(PROCESS_BUTTONS_STYLE)
        self.pushButton.setGeometry(QtCore.QRect(648, 10, 91, 26))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
	self.pushButton_2.setStyleSheet(PROCESS_BUTTONS_STYLE)
        self.pushButton_2.setGeometry(QtCore.QRect(648, 50, 91, 26))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
	self.pushButton_3.setStyleSheet(PROCESS_BUTTONS_STYLE)
        self.pushButton_3.setGeometry(QtCore.QRect(648, 90, 88, 26))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_11 = QtGui.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(480, 70, 61, 17))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.comboBox_2 = QtGui.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(575, 65, 51, 27))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
	self.comboBox_2.addItem(_fromUtf8(""))
        self.doubleSpinBox_4 = QtGui.QDoubleSpinBox(self.frame)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(515, 65, 62, 27))
        self.doubleSpinBox_4.setMaximum(999999999.0)
        self.doubleSpinBox_4.setObjectName(_fromUtf8("doubleSpinBox_4"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("MainWindow", "POSL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "During Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Before Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "After Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Light Source", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, "Blue")
        self.comboBox.setItemText(1, "IR")
        self.comboBox.setItemText(2, "AUX")
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Optical Power(%)", None, QtGui.QApplication.UnicodeUTF8))	
	self.label_14.setText(QtGui.QApplication.translate("MainWindow", "Channels", None, QtGui.QApplication.UnicodeUTF8)+':')
	self.label_15.setText("0")
	self.label_16.setText(QtGui.QApplication.translate("MainWindow", "Time per Chan", None, QtGui.QApplication.UnicodeUTF8)+':')
	self.label_17.setText("0 ms")  	
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "Number of Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Final Temperature (°C)", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Heating Rate (°C/s)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Stabilization (s)", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Accept", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "&Sample Info.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Time", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(0, "ms")
        self.comboBox_2.setItemText(1, "s")
	self.comboBox_2.setItemText(2, "us")


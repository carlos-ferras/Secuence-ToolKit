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
	x= mainScreenSize.width()/2-389
	y= mainScreenSize.height()/2-99
	Dialog.setGeometry(QtCore.QRect(x, y, 778, 198))
        Dialog.setMinimumSize(QtCore.QSize(778, 198))
        Dialog.setMaximumSize(QtCore.QSize(778, 198))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(6, 10, 676, 181))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
	self.frame.setStyleSheet(PROCESS_WIN_STYLE)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.frame)
        self.doubleSpinBox.setGeometry(QtCore.QRect(365, 135, 61, 27))
        self.doubleSpinBox.setMinimum(0.1)
        self.doubleSpinBox.setMaximum(20.0)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(240, 140, 131, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 151, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.frame)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(155, 135, 62, 27))
        self.doubleSpinBox_2.setMaximum(600.0)
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.line_2 = QtGui.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(10, 50, 656, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(10, 110,656, 21))
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
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(180, 20, 81, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.spinBox = QtGui.QSpinBox(self.frame)
        self.spinBox.setGeometry(QtCore.QRect(242, 16, 54, 27))
        self.spinBox.setMaximum(512)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label_11 = QtGui.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(320, 20, 61, 17))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.comboBox_2 = QtGui.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(416, 16, 55, 27))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
	self.comboBox_2.addItem(_fromUtf8(""))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(498, 20, 121, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
	self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(619, 20, 51, 17))
        self.label_6.setObjectName(_fromUtf8("label_4"))
        self.label_14 = QtGui.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(245, 80, 161, 17))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.spinBox_7 = QtGui.QSpinBox(self.frame)
        self.spinBox_7.setGeometry(QtCore.QRect(394, 76, 51, 27))
        self.spinBox_7.setMaximum(100)
        self.spinBox_7.setObjectName(_fromUtf8("spinBox_7"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(455, 140, 120, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.doubleSpinBox_3 = QtGui.QDoubleSpinBox(self.frame)	
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(560, 135, 62, 27))
        self.doubleSpinBox_3.setMaximum(999999999.0)
        self.doubleSpinBox_3.setObjectName(_fromUtf8("doubleSpinBox_3"))
        self.doubleSpinBox_4 = QtGui.QDoubleSpinBox(self.frame)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(356, 16, 62, 27))
        self.doubleSpinBox_4.setMaximum(999999999.0)
        self.doubleSpinBox_4.setObjectName(_fromUtf8("doubleSpinBox_4"))
        self.pushButton = QtGui.QPushButton(Dialog)
	self.pushButton.setStyleSheet(PROCESS_BUTTONS_STYLE)
        self.pushButton.setGeometry(QtCore.QRect(686, 10, 91, 26))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
	self.pushButton_2.setStyleSheet(PROCESS_BUTTONS_STYLE)
        self.pushButton_2.setGeometry(QtCore.QRect(686, 50, 91, 26))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
	self.pushButton_3.setStyleSheet(PROCESS_BUTTONS_STYLE)
        self.pushButton_3.setGeometry(QtCore.QRect(686, 90, 88, 26))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_12 = QtGui.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(10, 80, 151, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.spinBox_5 = QtGui.QSpinBox(self.frame)
        self.spinBox_5.setGeometry(QtCore.QRect(164, 76, 54, 27))
        self.spinBox_5.setMaximum(100)
        self.spinBox_5.setObjectName(_fromUtf8("spinBox_5"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("MainWindow", "LMOSL", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Heating Rate (°C/s)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Final Temperature (°C)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Ligth Source", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, "Blue")
        self.comboBox.setItemText(1, "IR")
        self.comboBox.setItemText(2, "AUX")
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Channels", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Time", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(0,  "ms")
        self.comboBox_2.setItemText(1, "s")
        self.comboBox_2.setItemText(2, "us")
	self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Time per Channel", None, QtGui.QApplication.UnicodeUTF8)+':')
	self.label_6.setText("0 ms")
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "End Optical Power (%)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Stabilization (s)", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Accept", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "&Sample Info.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Start Optical Power (%)", None, QtGui.QApplication.UnicodeUTF8))


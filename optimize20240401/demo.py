# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitle.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1140, 855)
        MainWindow.setStyleSheet("background-color: rgb(69, 69, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_graphics = QtWidgets.QWidget(self.centralwidget)
        self.widget_graphics.setGeometry(QtCore.QRect(-10, 0, 1151, 481))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_graphics.sizePolicy().hasHeightForWidth())
        self.widget_graphics.setSizePolicy(sizePolicy)
        self.widget_graphics.setMinimumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.widget_graphics.setFont(font)
        self.widget_graphics.setStyleSheet("background-color: rgb(46, 245, 255);")
        self.widget_graphics.setObjectName("widget_graphics")
        self.groupBox_1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_1.setGeometry(QtCore.QRect(0, 480, 811, 161))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_1.setFont(font)
        self.groupBox_1.setObjectName("groupBox_1")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 70, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("color: rgb(0, 170, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit_1.setGeometry(QtCore.QRect(170, 30, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setStyleSheet("color: rgb(0, 170, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.label_6 = QtWidgets.QLabel(self.groupBox_1)
        self.label_6.setGeometry(QtCore.QRect(30, 70, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(116, 116, 116);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_1)
        self.label_7.setGeometry(QtCore.QRect(30, 110, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(116, 116, 116);")
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.groupBox_1)
        self.label_4.setGeometry(QtCore.QRect(0, 70, 21, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_1)
        self.label_5.setGeometry(QtCore.QRect(0, 110, 21, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.label_1 = QtWidgets.QLabel(self.groupBox_1)
        self.label_1.setGeometry(QtCore.QRect(30, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("background-color: rgb(116, 116, 116);")
        self.label_1.setObjectName("label_1")
        self.label_3 = QtWidgets.QLabel(self.groupBox_1)
        self.label_3.setGeometry(QtCore.QRect(0, 30, 21, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 110, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("color: rgb(0, 170, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit_4.setGeometry(QtCore.QRect(510, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("color: rgb(0, 170, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit_5.setGeometry(QtCore.QRect(510, 110, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("color: rgb(0, 170, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_9 = QtWidgets.QLabel(self.groupBox_1)
        self.label_9.setGeometry(QtCore.QRect(420, 110, 81, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(116, 116, 116);\n"
"")
        self.label_9.setObjectName("label_9")
        self.label_2 = QtWidgets.QLabel(self.groupBox_1)
        self.label_2.setGeometry(QtCore.QRect(420, 30, 81, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(116, 116, 116);\n"
"")
        self.label_2.setObjectName("label_2")
        self.lcd_remaining_time_2 = QtWidgets.QLCDNumber(self.groupBox_1)
        self.lcd_remaining_time_2.setGeometry(QtCore.QRect(510, 30, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcd_remaining_time_2.sizePolicy().hasHeightForWidth())
        self.lcd_remaining_time_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lcd_remaining_time_2.setFont(font)
        self.lcd_remaining_time_2.setStyleSheet("color: rgb(0, 170, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.lcd_remaining_time_2.setSmallDecimalPoint(False)
        self.lcd_remaining_time_2.setObjectName("lcd_remaining_time_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_1)
        self.label_8.setGeometry(QtCore.QRect(420, 70, 81, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(116, 116, 116);\n"
"")
        self.label_8.setObjectName("label_8")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(810, 480, 331, 161))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_browse_src = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_browse_src.setGeometry(QtCore.QRect(12, 30, 93, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_browse_src.sizePolicy().hasHeightForWidth())
        self.pushButton_browse_src.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_browse_src.setFont(font)
        self.pushButton_browse_src.setObjectName("pushButton_browse_src")
        self.pb_load_sourceFile_submit = QtWidgets.QPushButton(self.groupBox_2)
        self.pb_load_sourceFile_submit.setGeometry(QtCore.QRect(200, 70, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pb_load_sourceFile_submit.setFont(font)
        self.pb_load_sourceFile_submit.setObjectName("pb_load_sourceFile_submit")
        self.lineEdit_source_path = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_source_path.setGeometry(QtCore.QRect(110, 30, 211, 28))
        self.lineEdit_source_path.setMinimumSize(QtCore.QSize(100, 20))
        self.lineEdit_source_path.setAutoFillBackground(False)
        self.lineEdit_source_path.setText("")
        self.lineEdit_source_path.setObjectName("lineEdit_source_path")
        self.pb_load_sourceFile_order = QtWidgets.QPushButton(self.groupBox_2)
        self.pb_load_sourceFile_order.setGeometry(QtCore.QRect(10, 70, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pb_load_sourceFile_order.setFont(font)
        self.pb_load_sourceFile_order.setObjectName("pb_load_sourceFile_order")
        self.pb_load_sourceFile_sure = QtWidgets.QPushButton(self.groupBox_2)
        self.pb_load_sourceFile_sure.setGeometry(QtCore.QRect(10, 110, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pb_load_sourceFile_sure.setFont(font)
        self.pb_load_sourceFile_sure.setObjectName("pb_load_sourceFile_sure")
        self.pb_load_sourceFile_cancel = QtWidgets.QPushButton(self.groupBox_2)
        self.pb_load_sourceFile_cancel.setGeometry(QtCore.QRect(200, 110, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pb_load_sourceFile_cancel.setFont(font)
        self.pb_load_sourceFile_cancel.setObjectName("pb_load_sourceFile_cancel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1140, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_1.setTitle(_translate("MainWindow", "显示信息"))
        self.label_6.setText(_translate("MainWindow", " 赤经（h:m:s）"))
        self.label_7.setText(_translate("MainWindow", " 赤纬（h:m:s）"))
        self.label_4.setText(_translate("MainWindow", "电"))
        self.label_5.setText(_translate("MainWindow", "源"))
        self.label_1.setText(_translate("MainWindow", " 当前恒星时"))
        self.label_3.setText(_translate("MainWindow", "射"))
        self.label_9.setText(_translate("MainWindow", "方位Alt"))
        self.label_2.setText(_translate("MainWindow", "观测时间"))
        self.label_8.setText(_translate("MainWindow", "俯仰Az"))
        self.groupBox_2.setTitle(_translate("MainWindow", "加载计划观测源文件"))
        self.pushButton_browse_src.setText(_translate("MainWindow", "浏 览"))
        self.pb_load_sourceFile_submit.setText(_translate("MainWindow", "提 交"))
        self.pb_load_sourceFile_order.setText(_translate("MainWindow", "排序"))
        self.pb_load_sourceFile_sure.setText(_translate("MainWindow", "确认"))
        self.pb_load_sourceFile_cancel.setText(_translate("MainWindow", "取消"))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\OneDrive\myGitHubProjects\fastworkApp\merge_workbooks\ui\fastwork.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(502, 535)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_filepath = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_filepath.setObjectName("lineEdit_filepath")
        self.gridLayout_2.addWidget(self.lineEdit_filepath, 0, 0, 1, 1)
        self.open_filepath = QtWidgets.QPushButton(self.centralwidget)
        self.open_filepath.setStyleSheet("font: 11pt \"黑体\";")
        self.open_filepath.setObjectName("open_filepath")
        self.gridLayout_2.addWidget(self.open_filepath, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setStyleSheet("font: 10pt \"黑体\";")
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushbutton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_start.setStyleSheet("background-color: rgb(7, 193, 96);\n"
"font: 11pt \"Agency FB\";\n"
"font: 11pt \"黑体\";")
        self.pushbutton_start.setObjectName("pushbutton_start")
        self.horizontalLayout.addWidget(self.pushbutton_start)
        self.pushbutton_openfolder = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_openfolder.setStyleSheet("background-color: rgb(7, 193, 96);\n"
"font: 11pt \"黑体\";")
        self.pushbutton_openfolder.setObjectName("pushbutton_openfolder")
        self.horizontalLayout.addWidget(self.pushbutton_openfolder)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setStyleSheet("font: 10pt \"黑体\";")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "人文互联网-高效办公工具分享"))
        self.open_filepath.setText(_translate("mainWindow", "选择文件夹"))
        self.checkBox.setText(_translate("mainWindow", "合并工作表"))
        self.pushbutton_start.setText(_translate("mainWindow", "开始合并"))
        self.pushbutton_openfolder.setText(_translate("mainWindow", "打开结果文件夹"))
        self.textEdit.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'黑体\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">左手excel,右手python，让你繁琐的工作自动化！</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">欢迎关注我的公众号：人文互联网！</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">回复关键词</span><span style=\" font-family:\'SimSun\'; font-weight:600; font-style:italic; color:#ff0000;\">&quot;高效办公&quot; </span><span style=\" font-family:\'SimSun\'; font-weight:600; color:#000000;\">即可获取下载链接。</span></p></body></html>"))
        self.label.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\"><img src=\":/qrcode/wechat_search.png\"/></p></body></html>"))
import imgcode_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

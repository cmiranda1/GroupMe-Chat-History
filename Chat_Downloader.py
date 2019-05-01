# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Chat_History import GroupMe
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        os.chdir(os.getcwd())
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(775, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.APIlabel = QtWidgets.QLabel(self.centralwidget)
        self.APIlabel.setObjectName("APIlabel")
        self.gridLayout.addWidget(self.APIlabel, 0, 0, 1, 1)
        self.FileNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.FileNameLabel.setObjectName("FileNameLabel")
        self.gridLayout.addWidget(self.FileNameLabel, 0, 1, 1, 1)
        self.APIdialogue = QtWidgets.QLineEdit(self.centralwidget)
        self.APIdialogue.setObjectName("APIdialogue")
        self.gridLayout.addWidget(self.APIdialogue, 1, 0, 1, 1)
        self.FileNamedialogue = QtWidgets.QLineEdit(self.centralwidget)
        self.FileNamedialogue.setObjectName("FileNamedialogue")
        self.gridLayout.addWidget(self.FileNamedialogue, 1, 1, 1, 1)
        self.APIkeyenter = QtWidgets.QPushButton(self.centralwidget)
        self.APIkeyenter.setObjectName("APIkeyenter")
        self.gridLayout.addWidget(self.APIkeyenter, 2, 0, 1, 1)
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setObjectName("SaveButton")
        self.gridLayout.addWidget(self.SaveButton, 2, 1, 1, 1)
        self.ChatListdd = QtWidgets.QComboBox(self.centralwidget)
        self.ChatListdd.setCurrentText("")
        self.ChatListdd.setObjectName("ChatListdd")
        self.gridLayout.addWidget(self.ChatListdd, 3, 0, 1, 2)
        self.Displaytable = QtWidgets.QTableWidget(self.centralwidget)
        self.Displaytable.setObjectName("Displaytable")
        self.gridLayout.addWidget(self.Displaytable, 4, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.APIkeyenter.clicked.connect(self.APIbuttonclick)
        self.APIkeyenter.clicked.connect(self.TableSample)
        self.SaveButton.clicked.connect(self.saveButtonClick)

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GroupMe Chat History Downloader -- Author: Colin Miranda"))
        self.APIlabel.setText(_translate("MainWindow", "GroupMe API Key"))
        self.FileNameLabel.setText(_translate("MainWindow", "Excel File Name"))
        self.APIkeyenter.setText(_translate("MainWindow", "Enter"))
        self.SaveButton.setText(_translate("MainWindow", "Save to Excel"))

    def APIbuttonclick(self):
        try:
            self.chats = GroupMe(token=self.APIdialogue.text()).getChats()
            self.ChatListdd.addItems(self.chats)
            chatname = str(self.ChatListdd.currentText())
            self.df = GroupMe(token=self.APIdialogue.text()).getDataFrame(chat_name=chatname,grouplist=self.chats)
        except:
            QtWidgets.QMessageBox.about('Warning','Incorret API Key')

    def saveButtonClick(self):
        try:
            filename = self.FileNamedialogue.text()
            self.df.to_excel(filename,index=False)
        except:
            print('Error')

    def TableSample(self):
        self.Displaytable.setColumnCount(6)
        self.Displaytable.setRowCount(100)
        self.Displaytable.setHorizontalHeaderLabels(['User ID','Name','Datetime','Text','Like List','Attachments'])
        for i in range(100):
            self.Displaytable.setItem(i, 0, QtWidgets.QTableWidgetItem(str(self.df['User ID'].iloc[i])))
            self.Displaytable.setItem(i, 1, QtWidgets.QTableWidgetItem(str(self.df['Name'].iloc[i])))
            self.Displaytable.setItem(i, 2, QtWidgets.QTableWidgetItem(str(self.df['Datetime'].iloc[i])))
            self.Displaytable.setItem(i, 3, QtWidgets.QTableWidgetItem(str(self.df['Text'].iloc[i])))
            self.Displaytable.setItem(i, 4, QtWidgets.QTableWidgetItem(str(self.df['Like List'].iloc[i])))
            self.Displaytable.setItem(i, 5, QtWidgets.QTableWidgetItem(str(self.df['Attachments'].iloc[i])))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
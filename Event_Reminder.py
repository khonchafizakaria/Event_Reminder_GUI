# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
import os.path

import pandas as pd

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox

class Ui_MainApp(QMainWindow):

    def __init__(self):

        super(Ui_MainApp, self).__init__()
        self.setupUi(self)
        self.frameGm = self.frameGeometry()
        self.screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        self.centerPoint = QtWidgets.QApplication.desktop().screenGeometry(self.screen).center()
        self.frameGm.moveCenter(self.centerPoint)
        self.move(self.frameGm.topLeft())
        self.setWindowTitle("Event Reminder")
        self.setWindowIcon(QtGui.QIcon("C:/Users/pc/Desktop/ER/icon.png"))

    def setupUi(self, MainApp):

        """ MainApp """

        MainApp.setObjectName("MainApp")
        MainApp.resize(600, 200)
        MainApp.setStyleSheet(
            "QWidget{color:black}\n"
            "QFrame{background-color:RoyalBlue}\n"
            "QPushButton{background-color:; color:white}\n"
            "QLabel {backround-color:None}\n"
            "QLineEdit{background-color:None}\n"
            "QTableWidget{background-color:None}\n")
        self.MainApp_CentralWidget = QtWidgets.QWidget(MainApp)
        self.MainApp_CentralWidget.setObjectName("MainApp_CentralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.MainApp_CentralWidget)
        self.verticalLayout.setObjectName("verticalLayout")

        """ WelcomeFrame"""

        self.WelcomeFrame = QtWidgets.QFrame(self.MainApp_CentralWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.WelcomeFrame.setFont(font)
        self.WelcomeFrame.setObjectName("WelcomeFrame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.WelcomeFrame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.WelcomemsgLb = QtWidgets.QLabel(self.WelcomeFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.WelcomemsgLb.setFont(font)
        self.WelcomemsgLb.setStyleSheet("color: rgb(255, 255, 255);")
        self.WelcomemsgLb.setAlignment(QtCore.Qt.AlignCenter)
        self.WelcomemsgLb.setObjectName("WelcomemsgLb")
        self.gridLayout_4.addWidget(self.WelcomemsgLb, 0, 1, 1, 2)
        self.CheckEventButton_W = QtWidgets.QPushButton(self.WelcomeFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CheckEventButton_W.setFont(font)
        self.CheckEventButton_W.setObjectName("CheckEventButton_W")
        self.gridLayout_4.addWidget(self.CheckEventButton_W, 1, 2, 1, 1)
        self.AddEventButton = QtWidgets.QPushButton(self.WelcomeFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AddEventButton.setFont(font)
        self.AddEventButton.setObjectName("AddEventButton")
        self.gridLayout_4.addWidget(self.AddEventButton, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.WelcomeFrame)

        """ AddEventFrame """

        self.AddEventFrame = QtWidgets.QFrame(self.MainApp_CentralWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AddEventFrame.setFont(font)
        self.AddEventFrame.setObjectName("AddEventFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.AddEventFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.AddEventFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setMinimumDate(QtCore.QDate(2018, 1, 1))
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setDateEditAcceptDelay(800)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_2.addWidget(self.calendarWidget, 4, 0, 1, 5)
        self.CheckEventButton = QtWidgets.QPushButton(self.AddEventFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CheckEventButton.setFont(font)
        self.CheckEventButton.setObjectName("CheckEventButton")
        self.gridLayout_2.addWidget(self.CheckEventButton, 5, 4, 1, 1)
        self.GobackAEButton = QtWidgets.QPushButton(self.AddEventFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.GobackAEButton.setFont(font)
        self.GobackAEButton.setObjectName("GobackAEButton")
        self.gridLayout_2.addWidget(self.GobackAEButton, 5, 3, 1, 1)
        self.ResetButton = QtWidgets.QPushButton(self.AddEventFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ResetButton.setFont(font)
        self.ResetButton.setObjectName("ResetButton")
        self.gridLayout_2.addWidget(self.ResetButton, 2, 4, 1, 1)
        self.EventnameLE = QtWidgets.QLineEdit(self.AddEventFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.EventnameLE.setFont(font)
        self.EventnameLE.setObjectName("EventnameLE")
        self.gridLayout_2.addWidget(self.EventnameLE, 2, 0, 1, 1)
        self.InsertEventButton = QtWidgets.QPushButton(self.AddEventFrame)
        self.InsertEventButton.setEnabled(False)
        self.InsertEventButton.setStyleSheet("background-color:grey")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.InsertEventButton.setFont(font)
        self.InsertEventButton.setObjectName("InsertEventButton")
        self.gridLayout_2.addWidget(self.InsertEventButton, 2, 3, 1, 1)
        self.EventDesLE = QtWidgets.QLineEdit(self.AddEventFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.EventDesLE.setFont(font)
        self.EventDesLE.setObjectName("EventDesLE")
        self.gridLayout_2.addWidget(self.EventDesLE, 2, 1, 1, 1)
        self.EventFileLE = QtWidgets.QLineEdit(self.AddEventFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.EventFileLE.setFont(font)
        self.EventFileLE.setObjectName("EventFileLE")
        self.gridLayout_2.addWidget(self.EventFileLE, 2, 2, 1, 1)
        self.verticalLayout.addWidget(self.AddEventFrame)

        """ CheckEventFrame """

        self.CheckEventFrame = QtWidgets.QFrame(self.MainApp_CentralWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CheckEventFrame.setFont(font)
        self.CheckEventFrame.setObjectName("CheckEventFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.CheckEventFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.TableWidget = QtWidgets.QTableWidget(self.CheckEventFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TableWidget.setFont(font)
        self.TableWidget.setObjectName("TableWidget")
        self.TableWidget.setColumnCount(0)
        self.TableWidget.setRowCount(0)
        self.gridLayout_3.addWidget(self.TableWidget, 1, 0, 2, 3)
        self.GobackCEButton = QtWidgets.QPushButton(self.CheckEventFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.GobackCEButton.setFont(font)
        self.GobackCEButton.setObjectName("GobackCEButton")
        self.gridLayout_3.addWidget(self.GobackCEButton, 3, 0, 1, 1)
        self.EventFileCELE = QtWidgets.QLineEdit(self.CheckEventFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.EventFileCELE.setFont(font)
        self.EventFileCELE.setObjectName("EventFileCELE")
        self.gridLayout_3.addWidget(self.EventFileCELE, 0, 0, 1, 2)
        self.FetchcsvButton = QtWidgets.QPushButton(self.CheckEventFrame)
        self.FetchcsvButton.setEnabled(False)
        self.FetchcsvButton.setStyleSheet("background-color:grey")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FetchcsvButton.setFont(font)
        self.FetchcsvButton.setObjectName("FetchcsvButton")
        self.gridLayout_3.addWidget(self.FetchcsvButton, 0, 2, 1, 1)
        self.DeleteEventButton = QtWidgets.QPushButton(self.CheckEventFrame)
        self.DeleteEventButton.setStyleSheet("background-color:grey")
        self.DeleteEventButton.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DeleteEventButton.setFont(font)
        self.DeleteEventButton.setObjectName("DeleteEventButton")
        self.gridLayout_3.addWidget(self.DeleteEventButton, 3, 1, 1, 1)
        self.Savecsv = QtWidgets.QPushButton(self.CheckEventFrame)
        self.Savecsv.setStyleSheet("background-color:grey")
        self.Savecsv.setEnabled(False)
        self.Savecsv.setObjectName("Savecsv")
        self.gridLayout_3.addWidget(self.Savecsv, 3, 2, 1, 1)
        self.verticalLayout.addWidget(self.CheckEventFrame)
        MainApp.setCentralWidget(self.MainApp_CentralWidget)

        """ statusbar """

        self.statusbar = QtWidgets.QStatusBar(MainApp)
        self.statusbar.setObjectName("statusbar")
        MainApp.setStatusBar(self.statusbar)

        """ Translation """

        self.retranslateUi(MainApp)
        QtCore.QMetaObject.connectSlotsByName(MainApp)

        """ Tab Order """

        MainApp.setTabOrder(self.AddEventButton, self.CheckEventButton_W)
        MainApp.setTabOrder(self.CheckEventButton_W, self.EventnameLE)
        MainApp.setTabOrder(self.EventnameLE, self.EventDesLE)
        MainApp.setTabOrder(self.EventDesLE, self.EventFileLE)
        MainApp.setTabOrder(self.EventFileLE, self.InsertEventButton)
        MainApp.setTabOrder(self.InsertEventButton, self.ResetButton)
        MainApp.setTabOrder(self.ResetButton, self.calendarWidget)
        MainApp.setTabOrder(self.calendarWidget, self.CheckEventButton)
        MainApp.setTabOrder(self.CheckEventButton, self.GobackAEButton)
        MainApp.setTabOrder(self.GobackAEButton, self.EventFileCELE)
        MainApp.setTabOrder(self.EventFileCELE, self.FetchcsvButton)
        MainApp.setTabOrder(self.FetchcsvButton, self.TableWidget)
        MainApp.setTabOrder(self.TableWidget, self.Savecsv)
        MainApp.setTabOrder(self.Savecsv, self.DeleteEventButton)
        MainApp.setTabOrder(self.DeleteEventButton, self.GobackCEButton)

        """ Frame Hiding """

        self.AddEventFrame.setHidden(True)
        self.CheckEventFrame.setHidden(True)
    
        """ Button Events """

        self.AddEventButton.clicked.connect(self.Show_AE_Frame)
        self.CheckEventButton_W.clicked.connect(self.Show_CE_Frame)
        
        self.GobackAEButton.clicked.connect(self.Show_Welcome_Frame)
        self.GobackCEButton.clicked.connect(self.Show_Welcome_Frame)

        self.EventnameLE.textChanged.connect(self.enable_insert_btn)
        self.EventDesLE.textChanged.connect(self.enable_insert_btn)
        self.EventFileLE.textChanged.connect(self.enable_insert_btn)

        self.InsertEventButton.clicked.connect(self.insert_data)
        self.ResetButton.clicked.connect(self.reset_inputs)
        self.CheckEventButton.clicked.connect(self.Show_CE_Frame)

        self.EventFileCELE.textChanged.connect(self.enable_fetch_save_delete)
        self.FetchcsvButton.clicked.connect(self.open_csv)
        self.DeleteEventButton.clicked.connect(self.del_event)
        self.Savecsv.clicked.connect(self.save_df)

    """ QFrame interactions """

    def reset_inputs(self):
        self.EventDesLE.clear()
        self.EventnameLE.clear()
        self.EventFileLE.clear()
    
    def Show_AE_Frame(self):
        self.AddEventFrame.setVisible(True)
        self.CheckEventFrame.setHidden(True)
        self.WelcomeFrame.setHidden(True)
        self.EventFileCELE.clear()
        self.TableWidget.clear()
        

    def Show_CE_Frame(self):
        self.CheckEventFrame.setVisible(True)
        self.AddEventFrame.setHidden(True)
        self.WelcomeFrame.setHidden(True)
        self.reset_inputs()
    
    def Show_Welcome_Frame(self):
        self.WelcomeFrame.setVisible(True)
        self.AddEventFrame.setHidden(True)
        self.CheckEventFrame.setHidden(True)
        self.EventFileCELE.clear()
        self.TableWidget.clear()
        self.reset_inputs()

    """ AddEvents_Functions """

    @QtCore.pyqtSlot()
    def enable_insert_btn(self):
        len_LE1 = len(self.EventnameLE.text())
        len_LE2 = len(self.EventDesLE.text())
        len_LE3 = len(self.EventFileLE.text())
        len_list = [len_LE1, len_LE2, len_LE3]

        for _len in len_list:
            if _len > 0:
                self.InsertEventButton.setEnabled(True)
                self.InsertEventButton.setStyleSheet("background-color:")
            else:
                self.InsertEventButton.setEnabled(False)
                self.InsertEventButton.setStyleSheet("background-color:grey")

        
    def insert_data(self):

        _name      = self.EventnameLE.text()
        _des       = self.EventDesLE.text()
        _date      = self.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)
        _EventFile = self.EventFileLE.text()
        _path      = "C:/EventReminder/"
        __path     = _path + "%s.csv"%(_EventFile) 
        _cols      = ["Event Name", "Event Description", "Event Date"]

        
        if not os.path.exists(_path):
            os.makedirs(_path)

        if os.path.isfile(__path):
            df0 = pd.read_csv(__path)
            df0.loc[-1, _cols[0]] = _name
            df0.loc[-1, _cols[1]] = _des
            df0.loc[-1, _cols[2]] = _date
            df0.to_csv(__path, index=False)
            self.statusbar.showMessage("Event inserted in %s" %(__path), 800)

        else:
            info = QMessageBox()
            info.setIcon(QMessageBox.Information)
            info.setText(u"No such file exists")
            info.setInformativeText("Do you want to create %s?" %(__path) )
            info.setWindowTitle(u"Missing file")
            info.setWindowIcon(QtGui.QIcon("C:/Users/pc/Desktop/ER/icon.png"))
            info.setStandardButtons(QMessageBox.Save|QMessageBox.Cancel)
            info.setDefaultButton(QMessageBox.Cancel)
            resp = info.exec_()
            if resp != QMessageBox.Save:
                return

            pd.DataFrame(columns=_cols,index=[]).to_csv(__path, index=False)

            df0 = pd.read_csv(__path)
            df0.loc[-1, _cols[0]] = _name
            df0.loc[-1, _cols[1]] = _des
            df0.loc[-1, _cols[2]] = _date
            df0.to_csv(__path, index=False)

            self.statusbar.showMessage(__path + " was created and populated.", 1100)
            
    """ CheckEvent_functions """
   
    @QtCore.pyqtSlot()
    def enable_fetch_save_delete(self):
        len_LE = len(self.EventFileCELE.text())
        if len_LE > 0:
            self.FetchcsvButton.setEnabled(True)
            self.FetchcsvButton.setStyleSheet("background-color:")
            self.Savecsv.setEnabled(True)
            self.Savecsv.setStyleSheet("background-color:")
            self.DeleteEventButton.setEnabled(True)
            self.DeleteEventButton.setStyleSheet("background-color:")
        else:
            self.FetchcsvButton.setEnabled(False)
            self.FetchcsvButton.setStyleSheet("background-color: grey")
            self.Savecsv.setEnabled(False)
            self.Savecsv.setStyleSheet("background-color: grey")
            self.DeleteEventButton.setEnabled(False)
            self.DeleteEventButton.setStyleSheet("background-color: grey")
    
    def open_csv(self):

        filepath = self.EventFileCELE.text()
        read_path = "C:/EventReminder/%s.csv"%(filepath)

        if os.path.isfile(read_path):
            df = pd.read_csv(read_path)
            self.TableWidget.setRowCount(len(df.index))
            self.TableWidget.setColumnCount(len(df.columns))

            for index in range(len(df.index)):
                for col in range(len(df.columns)):
                    self.TableWidget.setHorizontalHeaderLabels(df.columns)
                    self.TableWidget.setItem(
                        index, 
                        col, 
                        QtWidgets.QTableWidgetItem(df.iat[index, col])
                    )
                
            self.TableWidget.resizeColumnsToContents()
            self.TableWidget.resizeRowsToContents()
            self.TableWidget.setSortingEnabled(True)

        else:
            self.notification(
                QMessageBox.Warning,
                "Missing file", 
                "No such file exists.", 
                "Please check EventFile name or create a new one.",
                QMessageBox.Ok,)
    
    def del_event(self):

        indices    = self.TableWidget.selectionModel().selectedRows()
        index_list = [] 
        
        """ delete one event/row """
        for index in sorted(indices):
            self.TableWidget.removeRow(index.row())

        """ delete multiple events/rows """
        for model_index in indices:
            index = QtCore.QPersistentModelIndex(model_index)
            index_list.append(index)
        for index in index_list:
            self.TableWidget.removeRow(index.row())
      
    def save_df(self):

        proceed = QMessageBox.question(
			self, 
            'Overwriting action detected', 
            'Are you sure you want to overwrite the existing .csv file?',
            QMessageBox.Yes|QMessageBox.No, QMessageBox.No
		)
			
        if proceed != QMessageBox.Yes:
            return

        _path = self.EventFileCELE.text()
        save_path = "C:/EventReminder/%s.csv"%(_path)

        Dict = {}
        for col in range(self.TableWidget.columnCount()):
            items = []
            for row in range(self.TableWidget.rowCount()):
                it = self.TableWidget.item(row, col)
                items.append(it.text() if it is not None else "")
                h_item   = self.TableWidget.horizontalHeaderItem(col)
                H_column = str(col) if h_item is None else h_item.text()
                Dict[H_column] = items

        save_df = pd.DataFrame(data=Dict)

        if save_df.empty: #check if df is empty

            """ Saving an empty df will raise an Error upon its read,
            so we'll avoid that Error by parsing the columns into the empty df.
            When later on when we try to insert a new event, the df already has columns
            to parse into. """

            _cols = ["Event Name", "Event Description", "Event Date"]

            pd.DataFrame(columns=_cols,index=[]).to_csv(save_path ,index=False)

            self.notification(
                QMessageBox.Information,
                "Overwriting action", 
                "Successful", 
                "Your EventFile has been saved.",
                QMessageBox.Ok,)

        else:
            save_df.to_csv(save_path,index=False)

            self.notification(
                QMessageBox.Information,
                "Overwriting action", 
                "Successful", 
                "Your EventFile has been saved.",
                QMessageBox.Ok,)

    """ Notification : used for informative QMessageBoxes (warning, information, ...) 
        that have no impact on the program (CheckEvent missing file, CheckEvent successful saving) """

    def notification(self, _type, windowtitle, text, info_text,  button):
        box  = QMessageBox()
        box.setIcon(_type)
        box.setWindowTitle(windowtitle)
        box.setText(text)
        box.setInformativeText(info_text)
        box.setStandardButtons(button)
        box.setWindowIcon(QtGui.QIcon("C:/Users/pc/Desktop/Event_Reminder_GUI/icon.png"))
        resp = box.exec_()
        
    """ Translation """

    def retranslateUi(self, MainApp):
        _translate = QtCore.QCoreApplication.translate
        MainApp.setWindowTitle(_translate("MainApp", "MainWindow"))
        self.WelcomemsgLb.setText(_translate("MainApp", "Welcome to Event Reminder"))
        self.CheckEventButton_W.setText(_translate("MainApp", "Check Events"))
        self.AddEventButton.setText(_translate("MainApp", "Add Events"))
        self.CheckEventButton.setText(_translate("MainApp", "Check Events"))
        self.GobackAEButton.setText(_translate("MainApp", "Go Back"))
        self.ResetButton.setText(_translate("MainApp", "Reset"))
        self.EventnameLE.setPlaceholderText(_translate("MainApp", "Enter Event name:"))
        self.InsertEventButton.setText(_translate("MainApp", "Insert"))
        self.EventDesLE.setPlaceholderText(_translate("MainApp", "Enter Event Description:"))
        self.EventFileLE.setPlaceholderText(_translate("MainApp", "Enter EventFile name:"))
        self.GobackCEButton.setText(_translate("MainApp", "Go Back"))
        self.EventFileCELE.setPlaceholderText(_translate("MainApp", "Enter EventFile:"))
        self.FetchcsvButton.setText(_translate("MainApp", "Fetch CSV"))
        self.DeleteEventButton.setText(_translate("MainApp", "Delete Event"))
        self.Savecsv.setText(_translate("MainApp", "Save CSV"))

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Ui_MainApp()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui_files/tabu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from core.meta_heuristics.tabu_search.tabu_search import measure_tabu
from core.graph import graph



class Ui_tabuScreen(object):
    def setupUi(self, tabuScreen):
        tabuScreen.setObjectName("tabuScreen")
        tabuScreen.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(tabuScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.browseCsvButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseCsvButton.setGeometry(QtCore.QRect(480, 180, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.browseCsvButton.setFont(font)
        self.browseCsvButton.setStyleSheet("background-color: rgb(24, 53, 76);\n"
"color: rgb(230, 236, 235);")
        self.browseCsvButton.setObjectName("browseCsvButton")
        self.screenTitle = QtWidgets.QLabel(self.centralwidget)
        self.screenTitle.setGeometry(QtCore.QRect(330, 40, 500, 71))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.screenTitle.setFont(font)
        self.screenTitle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.screenTitle.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(24, 53, 75);\n"
"")
        self.screenTitle.setObjectName("screenTitle")
        self.filename = QtWidgets.QLineEdit(self.centralwidget)
        self.filename.setGeometry(QtCore.QRect(130, 180, 341, 31))
        self.filename.setText("")
        self.filename.setObjectName("filename")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(130, 340, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.submitButton.setFont(font)
        self.submitButton.setStyleSheet("background-color: rgb(24, 53, 76);\n"
"color: rgb(230, 236, 235);")
        self.submitButton.setObjectName("submitButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 250, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(24, 53, 75);\n"
"")
        self.label.setObjectName("label")
        self.colorsInput = QtWidgets.QSpinBox(self.centralwidget)
        self.colorsInput.setGeometry(QtCore.QRect(270, 250, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.colorsInput.setFont(font)
        self.colorsInput.setMaximum(50000)
        self.colorsInput.setObjectName("colorsInput")
        self.repsInput = QtWidgets.QSpinBox(self.centralwidget)
        self.repsInput.setGeometry(QtCore.QRect(560, 250, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.repsInput.setFont(font)
        self.repsInput.setMaximum(50000)
        self.repsInput.setObjectName("repsInput")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 250, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(24, 53, 75);\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 290, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(24, 53, 75);\n"
"")
        self.label_3.setObjectName("label_3")
        self.iteartionsInput = QtWidgets.QSpinBox(self.centralwidget)
        self.iteartionsInput.setGeometry(QtCore.QRect(270, 290, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.iteartionsInput.setFont(font)
        self.iteartionsInput.setMaximum(50000)
        self.iteartionsInput.setObjectName("iteartionsInput")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 290, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(24, 53, 75);\n"
"")
        self.label_4.setObjectName("label_4")
        self.tabusizeInput = QtWidgets.QSpinBox(self.centralwidget)
        self.tabusizeInput.setGeometry(QtCore.QRect(560, 290, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.tabusizeInput.setFont(font)
        self.tabusizeInput.setMaximum(50000)
        self.tabusizeInput.setObjectName("tabusizeInput")
        self.resultLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.resultLabel1.setGeometry(QtCore.QRect(130, 400, 200, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.resultLabel1.setFont(font)
        self.resultLabel1.setObjectName("resultLabel1")
        self.result1 = QtWidgets.QLabel(self.centralwidget)
        self.result1.setGeometry(QtCore.QRect(330, 400, 250, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.result1.setFont(font)
        self.result1.setObjectName("result1")
        self.resultLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.resultLabel2.setGeometry(QtCore.QRect(130, 460, 200, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.resultLabel2.setFont(font)
        self.resultLabel2.setObjectName("resultLabel2")
        self.result2 = QtWidgets.QLabel(self.centralwidget)
        self.result2.setGeometry(QtCore.QRect(330, 460, 250, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.result2.setFont(font)
        self.result2.setObjectName("result2")
        self.returnButton = QtWidgets.QPushButton(self.centralwidget)
        self.returnButton.setGeometry(QtCore.QRect(130, 500, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.returnButton.setFont(font)
        self.returnButton.setStyleSheet("background-color: rgb(24, 53, 76);\n"
"color: rgb(230, 236, 235);")
        self.returnButton.setObjectName("returnButton")
        self.refrechButton = QtWidgets.QPushButton(self.centralwidget)
        self.refrechButton.setGeometry(QtCore.QRect(480, 500, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.refrechButton.setFont(font)
        self.refrechButton.setStyleSheet("background-color: rgb(24, 53, 76);\n"
"color: rgb(230, 236, 235);")
        self.refrechButton.setObjectName("refrechButton")
        tabuScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(tabuScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        tabuScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(tabuScreen)
        self.statusbar.setObjectName("statusbar")
        tabuScreen.setStatusBar(self.statusbar)

        self.retranslateUi(tabuScreen)
        QtCore.QMetaObject.connectSlotsByName(tabuScreen)
        self.browseCsvButton.clicked.connect(partial(self.browseClicked))
        self.submitButton.clicked.connect(partial(self.submitClicked))
        self.refrechButton.clicked.connect(partial(self.refreshClicked))

        
    def retranslateUi(self, tabuScreen):
        _translate = QtCore.QCoreApplication.translate
        tabuScreen.setWindowTitle(_translate("tabuScreen", "MainWindow"))
        self.browseCsvButton.setText(_translate("tabuScreen", "Browse CSV file"))
        self.screenTitle.setText(_translate("tabuScreen", "TABU"))
        self.submitButton.setText(_translate("tabuScreen", "Show result"))
        self.label.setText(_translate("tabuScreen", "Colors number"))
        self.label_2.setText(_translate("tabuScreen", "Repetitions"))
        self.label_3.setText(_translate("tabuScreen", "Max iterations"))
        self.label_4.setText(_translate("tabuScreen", "Tabu size"))
        self.resultLabel1.setText(_translate("tabuScreen", "Number Of Colors"))
        self.result1.setText(_translate("tabuScreen", "0"))
        self.resultLabel2.setText(_translate("tabuScreen", "Execution Time"))
        self.result2.setText(_translate("tabuScreen", "0"))
        self.returnButton.setText(_translate("tabuScreen", "Return"))
        self.refrechButton.setText(_translate("tabuScreen", "Refresh"))

    def browseClicked(self):
        print('browse clicked')
        fname  = QFileDialog.getOpenFileName(None,"Open File","")
        if fname:
                self.filename.setText(str(fname[0]))

    def submitClicked(self):
        print('submit clicked')
        g = graph()
        g.read(self.filename.text())
        param_colors_number = self.colorsInput.value()
        param_reps = self.repsInput.value()
        param_max_iterations = self.iteartionsInput.value()
        param_tabu_size = self.tabusizeInput.value()
        
        result = measure_tabu(g,param_colors_number,param_tabu_size,param_reps,param_max_iterations)
        self.result1.setText(str(result[0]))
        self.result2.setText("{:.9}s".format(result[1]))
        g.visualize_graph()
   
        
    def refreshClicked(self):
        self.filename.setText("")
        self.repsInput.setValue(0)
        self.colorsInput.setValue(0)
        self.iteartionsInput.setValue(0)
        self.tabusizeInput.setValue(0)
        self.result1.setText("-")
        self.result2.setText("-")
              
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tabuScreen = QtWidgets.QMainWindow()
    ui = Ui_tabuScreen()
    ui.setupUi(tabuScreen)
    tabuScreen.show()
    sys.exit(app.exec_())

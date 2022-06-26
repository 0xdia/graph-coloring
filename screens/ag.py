# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './screens/ui_files/ag.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from core.meta_heuristics.genetic_algorithm.genetic_algorithm import (
    measure_genetic_algorithm,
)
from core.graph import graph


class Ui_agScreen(object):
    def setupUi(self, agScreen):
        agScreen.setObjectName("agScreen")
        agScreen.resize(860, 600)
        self.centralwidget = QtWidgets.QWidget(agScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.resultLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.resultLabel1.setGeometry(QtCore.QRect(160, 400, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.resultLabel1.setFont(font)
        self.resultLabel1.setObjectName("resultLabel1")
        self.browseCsvButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseCsvButton.setGeometry(QtCore.QRect(490, 120, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.browseCsvButton.setFont(font)
        self.browseCsvButton.setStyleSheet(
            "background-color: rgb(24, 53, 76);\n" "color: rgb(230, 236, 235);"
        )
        self.browseCsvButton.setObjectName("browseCsvButton")
        self.poolsizeLabel = QtWidgets.QLabel(self.centralwidget)
        self.poolsizeLabel.setGeometry(QtCore.QRect(100, 180, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.poolsizeLabel.setFont(font)
        self.poolsizeLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.poolsizeLabel.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: rgb(24, 53, 75);\n" ""
        )
        self.poolsizeLabel.setObjectName("poolsizeLabel")
        self.iterationsLabel = QtWidgets.QLabel(self.centralwidget)
        self.iterationsLabel.setGeometry(QtCore.QRect(430, 180, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.iterationsLabel.setFont(font)
        self.iterationsLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.iterationsLabel.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: rgb(24, 53, 75);\n" ""
        )
        self.iterationsLabel.setObjectName("iterationsLabel")
        self.returnButton = QtWidgets.QPushButton(self.centralwidget)
        self.returnButton.setGeometry(QtCore.QRect(150, 500, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.returnButton.setFont(font)
        self.returnButton.setStyleSheet(
            "background-color: rgb(24, 53, 76);\n" "color: rgb(230, 236, 235);"
        )
        self.returnButton.setObjectName("returnButton")
        self.resultLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.resultLabel2.setGeometry(QtCore.QRect(160, 440, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.resultLabel2.setFont(font)
        self.resultLabel2.setObjectName("resultLabel2")
        self.result1 = QtWidgets.QLabel(self.centralwidget)
        self.result1.setGeometry(QtCore.QRect(360, 400, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.result1.setFont(font)
        self.result1.setObjectName("result1")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(160, 360, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.submitButton.setFont(font)
        self.submitButton.setStyleSheet(
            "background-color: rgb(24, 53, 76);\n" "color: rgb(230, 236, 235);"
        )
        self.submitButton.setObjectName("submitButton")
        self.screenTitle = QtWidgets.QLabel(self.centralwidget)
        self.screenTitle.setGeometry(QtCore.QRect(170, 20, 441, 71))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.screenTitle.setFont(font)
        self.screenTitle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.screenTitle.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: rgb(24, 53, 75);\n" ""
        )
        self.screenTitle.setObjectName("screenTitle")
        self.iterationsInput = QtWidgets.QSpinBox(self.centralwidget)
        self.iterationsInput.setGeometry(QtCore.QRect(590, 180, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.iterationsInput.setFont(font)
        self.iterationsInput.setMaximum(50000)
        self.iterationsInput.setObjectName("iterationsInput")
        self.filename = QtWidgets.QLineEdit(self.centralwidget)
        self.filename.setGeometry(QtCore.QRect(140, 120, 341, 31))
        self.filename.setText("")
        self.filename.setObjectName("filename")
        self.refrechButton = QtWidgets.QPushButton(self.centralwidget)
        self.refrechButton.setGeometry(QtCore.QRect(510, 500, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.refrechButton.setFont(font)
        self.refrechButton.setStyleSheet(
            "background-color: rgb(24, 53, 76);\n" "color: rgb(230, 236, 235);"
        )
        self.refrechButton.setObjectName("refrechButton")
        self.result2 = QtWidgets.QLabel(self.centralwidget)
        self.result2.setGeometry(QtCore.QRect(360, 440, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.result2.setFont(font)
        self.result2.setObjectName("result2")
        self.poolsizeInput = QtWidgets.QSpinBox(self.centralwidget)
        self.poolsizeInput.setGeometry(QtCore.QRect(260, 180, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.poolsizeInput.setFont(font)
        self.poolsizeInput.setMaximum(50000)
        self.poolsizeInput.setObjectName("poolsizeInput")
        self.crossprobaLabel = QtWidgets.QLabel(self.centralwidget)
        self.crossprobaLabel.setGeometry(QtCore.QRect(50, 310, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.crossprobaLabel.setFont(font)
        self.crossprobaLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.crossprobaLabel.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: rgb(24, 53, 75);\n" ""
        )
        self.crossprobaLabel.setObjectName("crossprobaLabel")
        self.crossprobaInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.crossprobaInput.setGeometry(QtCore.QRect(180, 310, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.crossprobaInput.setFont(font)
        self.crossprobaInput.setMaximum(1.0)
        self.crossprobaInput.setSingleStep(0.1)
        self.crossprobaInput.setObjectName("crossprobaInput")
        self.mutationprobaLabel = QtWidgets.QLabel(self.centralwidget)
        self.mutationprobaLabel.setGeometry(QtCore.QRect(280, 310, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.mutationprobaLabel.setFont(font)
        self.mutationprobaLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mutationprobaLabel.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: rgb(24, 53, 75);\n" ""
        )
        self.mutationprobaLabel.setObjectName("mutationprobaLabel")
        self.mutationprobaInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.mutationprobaInput.setGeometry(QtCore.QRect(440, 310, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.mutationprobaInput.setFont(font)
        self.mutationprobaInput.setMaximum(1.0)
        self.mutationprobaInput.setSingleStep(0.1)
        self.mutationprobaInput.setObjectName("mutationprobaInput")
        self.selectionperLabel = QtWidgets.QLabel(self.centralwidget)
        self.selectionperLabel.setGeometry(QtCore.QRect(540, 310, 151, 31))

        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.selectionperLabel.setFont(font)
        self.selectionperLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.selectionperLabel.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: rgb(24, 53, 75);\n" ""
        )
        self.selectionperLabel.setObjectName("selectionperLabel")
        self.selectionperInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.selectionperInput.setGeometry(QtCore.QRect(700, 310, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.selectionperInput.setFont(font)
        self.selectionperInput.setMaximum(1.0)
        self.selectionperInput.setSingleStep(0.1)
        self.selectionperInput.setObjectName("selectionperInput")
        self.crossingmanerLabel = QtWidgets.QLabel(self.centralwidget)
        self.crossingmanerLabel.setGeometry(QtCore.QRect(50, 230, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.crossingmanerLabel.setFont(font)
        self.crossingmanerLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.crossingmanerLabel.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: rgb(24, 53, 75);\n" ""
        )
        self.crossingmanerLabel.setObjectName("crossingmanerLabel")
        self.selectionstrLabel = QtWidgets.QLabel(self.centralwidget)
        self.selectionstrLabel.setGeometry(QtCore.QRect(430, 230, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.selectionstrLabel.setFont(font)
        self.selectionstrLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.selectionstrLabel.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: rgb(24, 53, 75);\n" ""
        )
        self.selectionstrLabel.setObjectName("selectionstrLabel")
        self.selectionstrInput = QtWidgets.QComboBox(self.centralwidget)
        self.selectionstrInput.addItem("roulette")
        self.selectionstrInput.addItem("ranking")
        self.selectionstrInput.setGeometry(QtCore.QRect(590, 230, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.selectionstrInput.setFont(font)
        self.selectionstrInput.setMaxVisibleItems(5)
        self.selectionstrInput.setObjectName("selectionstrInput")
        self.uniformButton = QtWidgets.QRadioButton(self.centralwidget)
        self.uniformButton.setGeometry(QtCore.QRect(220, 230, 95, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.uniformButton.setFont(font)
        self.uniformButton.setObjectName("uniformButton")
        self.kButton = QtWidgets.QRadioButton(self.centralwidget)
        self.kButton.setGeometry(QtCore.QRect(220, 260, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.kButton.setFont(font)
        self.kButton.setObjectName("kButton")
        self.knumberInput = QtWidgets.QSpinBox(self.centralwidget)
        self.knumberInput.setGeometry(QtCore.QRect(270, 260, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.knumberInput.setFont(font)
        self.knumberInput.setMaximum(50)
        self.knumberInput.setObjectName("knumberInput")
        agScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(agScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 26))
        self.menubar.setObjectName("menubar")
        agScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(agScreen)
        self.statusbar.setObjectName("statusbar")
        agScreen.setStatusBar(self.statusbar)

        self.retranslateUi(agScreen)
        QtCore.QMetaObject.connectSlotsByName(agScreen)
        self.submitButton.clicked.connect(partial(self.submitClicked))
        self.browseCsvButton.clicked.connect(partial(self.browseClicked))

    def retranslateUi(self, agScreen):
        _translate = QtCore.QCoreApplication.translate
        agScreen.setWindowTitle(_translate("agScreen", "MainWindow"))
        self.resultLabel1.setText(_translate("agScreen", "Number Of Colors"))
        self.browseCsvButton.setText(_translate("agScreen", "Browse CSV file"))
        self.poolsizeLabel.setText(_translate("agScreen", "Pool Size"))
        self.iterationsLabel.setText(_translate("agScreen", "Iterations"))
        self.returnButton.setText(_translate("agScreen", "Return"))
        self.resultLabel2.setText(_translate("agScreen", "Execution Time"))
        self.result1.setText(_translate("agScreen", "0"))
        self.submitButton.setText(_translate("agScreen", "Show result"))
        self.screenTitle.setText(_translate("agScreen", "Genetic Algorithm"))
        self.refrechButton.setText(_translate("agScreen", "Refresh"))
        self.result2.setText(_translate("agScreen", "0"))
        self.crossprobaLabel.setText(_translate("agScreen", "Cross Proba"))
        self.mutationprobaLabel.setText(_translate("agScreen", "Mutation Proba"))
        self.selectionperLabel.setText(_translate("agScreen", "Selection Pers"))
        self.crossingmanerLabel.setText(_translate("agScreen", "Crossing Maner"))
        self.selectionstrLabel.setText(_translate("agScreen", "Selection Str"))
        self.uniformButton.setText(_translate("agScreen", "Uniform"))
        self.kButton.setText(_translate("agScreen", "K"))

    def browseClicked(self):
        print("browse clicked")
        fname = QFileDialog.getOpenFileName(None, "Open File", "")
        if fname:
            self.filename.setText(str(fname[0]))

    def submitClicked(self):
        print("submit clicked")
        poolsize = self.poolsizeInput.value()
        iterations = self.iterationsInput.value()
        selectionStrategy = self.selectionstrInput.currentText()
        crossProba = self.crossprobaInput.value()
        mutationProba = self.mutationprobaInput.value()
        selectionPercentage = self.selectionperInput.value()
        crossingManer = "uniform"
        if self.kButton.isChecked():
            crossingManer = str(self.knumberInput.value())

        g = graph()
        g.read(self.filename.text())
        result = measure_genetic_algorithm(
            g,
            poolsize,
            selectionStrategy,
            selectionPercentage,
            crossProba,
            crossingManer,
            mutationProba,
            iterations,
        )
        self.result1.setText(str(result[0]))
        self.result2.setText("{:.9}s".format(result[1]))
        g.visualize_graph()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    agScreen = QtWidgets.QMainWindow()
    ui = Ui_agScreen()
    ui.setupUi(agScreen)
    agScreen.show()
    sys.exit(app.exec_())

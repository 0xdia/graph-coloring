import sys
from PyQt5 import QtWidgets
from screens.bbScreen import Ui_bbScreen

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    bbScreen = QtWidgets.QMainWindow()
    ui = Ui_bbScreen()
    ui.setupUi(bbScreen)
    bbScreen.show()
    sys.exit(app.exec_())

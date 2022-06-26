import sys
from PyQt5 import QtWidgets
from screens.bbScreen import Ui_bbScreen
from screens.tabu import Ui_tabuScreen
from screens.rlf import Ui_rlfScreen
from screens.dsatur import Ui_dsaturScreen

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dsaturScreen = QtWidgets.QMainWindow()
    ui = Ui_dsaturScreen()
    ui.setupUi(dsaturScreen)
    dsaturScreen.show()
    sys.exit(app.exec_())


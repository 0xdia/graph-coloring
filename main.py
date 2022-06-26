import sys
from PyQt5 import QtWidgets
from screens.bbScreen import Ui_bbScreen
from screens.tabu import Ui_tabuScreen

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    tabuScreen = QtWidgets.QMainWindow()
    ui = Ui_tabuScreen()
    ui.setupUi(tabuScreen)
    tabuScreen.show()
    sys.exit(app.exec_())

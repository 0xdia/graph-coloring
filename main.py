import sys
from PyQt5 import QtWidgets
from screens.bbScreen import Ui_bbScreen
from screens.tabu import Ui_tabuScreen
from screens.rlf import Ui_rlfScreen
from screens.dsatur import Ui_dsaturScreen
from screens.benchmark import Ui_benchmarkScreen
from screens.home import Ui_MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


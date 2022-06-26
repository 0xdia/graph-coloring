from PyQt5 import QtWidgets
import sys
from screens.home import Ui_MainWindow

pile= []
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setFixedHeight(600)
    MainWindow.setFixedWidth(800)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,pile)
    MainWindow.show()
    sys.exit(app.exec_())

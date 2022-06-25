from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from widgets.menu_button import menu_button

from views.BranchAndBound import branchTab

class HomeScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title of main window
        self.setWindowTitle('Knapsack algorithms')

        # set the size of window
        self.Width = 1024
        self.height = int(0.618 * self.Width)
        self.setFixedSize(self.Width, self.height)

        # add all widgets
        self.home = menu_button('Home', self)
        self.branch = menu_button('Branch and bound', self)
        self.dynamic = menu_button('Dynamic Programming', self)
        self.greedy = menu_button('Greedy heuristic', self)
        self.hill = menu_button('Hill Climbing heuristic', self)

        self.home.clicked.connect(self.showHome)
        self.branch.clicked.connect(self.showBranch)
        self.dynamic.clicked.connect(self.showDynamic)
        self.greedy.clicked.connect(self.showGreedy)
        self.hill.clicked.connect(self.showHill)

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Knapsack algorithms')
        self.setWindowIcon(QIcon('./images/knapsack.png'))

        menu_layout = QVBoxLayout()

        menu_layout.addWidget(self.home)
        menu_layout.addWidget(self.branch)
        menu_layout.addWidget(self.dynamic)
        menu_layout.addWidget(self.greedy)
        menu_layout.addWidget(self.hill)
        menu_layout.addStretch(0)
        menu_layout.setSpacing(0)
        menu_widget = QWidget()
        menu_widget.setStyleSheet(
            "QWidget"
            "{"
            "background-color : #00CED1;"
            "border-radius: 12px;"
            "}"
        )
        menu_widget.setLayout(menu_layout)

        self.tab_widget = QTabWidget()
        self.tab_widget.setObjectName('tab_widget')

        self.tab_widget.addTab(self.homeTab(), '')
        self.tab_widget.addTab(branchTab(self), '')
        self.tab_widget.addTab(self.dynamicTab(), '')
        self.tab_widget.addTab(self.greedyTab(), '')
        self.tab_widget.addTab(self.hillTab(), '')

        self.tab_widget.setCurrentIndex(0)
        self.tab_widget.setStyleSheet(
            "QTabBar::tab"
            "{"
            "width: 0px;"
            "height: 0px;"
            "}"
        )

        main_layout = QHBoxLayout()

        main_layout.addWidget(menu_widget)
        main_layout.addWidget(self.tab_widget)

        main_widget = QWidget()
        main_widget.setStyleSheet("QWidget"
                                  "{"

                                  "background-color : #E6E6E6;"
                                  "border: none;"
                                  "margin: 0px;"
                                  "padding: 0px;"
                                  "color: #000;"

                                  "}"
                                  )

        main_widget.setObjectName('main_widget')
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    # buttons
    def showHome(self):
        self.tab_widget.setCurrentIndex(0)

    def showBranch(self):
        self.tab_widget.setCurrentIndex(1)

    def showDynamic(self):
        self.tab_widget.setCurrentIndex(2)

    def showGreedy(self):
        self.tab_widget.setCurrentIndex(3)

    def showHill(self):
        self.tab_widget.setCurrentIndex(4)

    # -----------------
    # pages
    def homeTab(self):
        main_layout = QVBoxLayout()
        welcome = QLabel('Welcome To The Knapsack-Problem Solver')
        welcome.setStyleSheet(
            "QLabel"
            "{"
            "font-size: 32px;"
            "font-weight: bold;"
            "color: #000;"
            "}"
        )

        by = QLabel('Resolving the Knapsack Problem, by:')
        by.setStyleSheet(
            "QLabel"
            "{"
            "font-size: 18px;"
            "margin-top: 20px;"
            "color: #000;"
            "}"
        )

        memebers = QLabel('''
            <ul>
                <li>Mohamed Amine </li>
                <li style="margin-top:8px;">Haddad zineddine</li>
                <li style="margin-top:8px;">Mohamed Abdelkader</li>
              

            </ul>
        ''')
        memebers.setStyleSheet(
            "QLabel"
            "{"
            "font-size: 16px;"
            "margin-top: 12px;"
            "color: #000;"
            "}"
        )

        label = QLabel(self)
        pixmap = QPixmap('./images/home.jpeg')
        pixmap = pixmap.scaled(300, 300)

        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(
            "QLabel"
            "{"
            "margin-top: 50px;"
            "}"
        )

        main_layout.addWidget(welcome)
        main_layout.addWidget(by)
        main_layout.addWidget(memebers)
        main_layout.addWidget(label)

        main_layout.addStretch(5)
        main = QWidget()

        main.setLayout(main_layout)
        return main 

    def dynamicTab(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('Dynamic programming'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def greedyTab(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('Greedy heuristic'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def hillTab(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('Hill Climbing heuristic'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

  


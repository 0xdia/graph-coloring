from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from core.exact_methods.branch_and_bound import measured_branch_and_bound
from core.graph import graph

from widgets.calculte_button import calculte_button
from widgets.upload_button import upload_button
from widgets.table_view import table_view


def run(self):
    g = graph()
    print("file< ", self.fname[:len(self.fname)])
    g.read(self.fname[:len(self.fname)])
    
    optimum, exec_time = measured_branch_and_bound(g)

    data = {
        'Nombre de couleur optimal': [str(optimum)],
        "Temps d'execution": [str(exec_time)],
    }

    showResult(self, data)


def branchTab(self):
    self.main_layout = QVBoxLayout()
    welcome = QLabel('Branch and bound')
    welcome.setStyleSheet(
        "QLabel"
        "{"
        "font-size: 32px;"
        "font-weight: bold;"
        "color: #000;"
        "}"
    )

    container = QHBoxLayout()
    container.setContentsMargins(0, 0, 0, 0)

    maxWeight = QLineEdit(self)
    maxWeight.setPlaceholderText('Max Weight')
    maxWeight.setFixedHeight(80)

    maxWeight.setStyleSheet(
        "QLineEdit"
        "{"
        "border: 1px solid #000;"
        "border-radius: 12px;"
        "font-weight: bold;"
        "padding: 5px;"
        "}"
    )

    input_file = upload_button('Upload col file', self)
    input_file.setFixedWidth(120)
    input_file.setFixedHeight(80)

    input_file.clicked.connect(lambda: uploadFile(self))

    container.addWidget(maxWeight)
    container.addWidget(input_file)

    upload = QWidget()
    upload.setLayout(container)

    upload.setStyleSheet(
        "QWidget"
        "{"
        "margin-top: 40px;"
        "}"
    )

    self.main_layout.addWidget(welcome)
    self.main_layout.addWidget(upload)

    calcualte = calculte_button('Calculate', self)

    calcualte.clicked.connect(lambda: run(
        self))

    calcualte.setFixedWidth(300)
    calcualte.setFixedHeight(80)

    self.main_layout.addWidget(calcualte)

    self.main_layout.addStretch(5)
    main = QWidget()
    main.setLayout(self.main_layout)
    return main


def uploadFile(self):
    fname, _ = QFileDialog.getOpenFileName(
        self, "Import Col", "", "Col input files (*.*)")
    self.fname = fname


def showResult(self, data):
    self.table = table_view(data, 2, 2)
    self.table.verticalHeader().setVisible(False)
    self.table.setStyleSheet(
        "QTableView"
        "{"
        "margin-right: 10px;"
        "margin-top: 40px;"
        "}"
    )
    header = self.table.horizontalHeader()
    header.setMaximumWidth(760)
    header.setSectionResizeMode(0, QHeaderView.Stretch)

    self.table.setFixedWidth(1200)

    self.main_layout.addWidget(self.table)

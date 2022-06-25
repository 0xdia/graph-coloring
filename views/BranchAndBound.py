from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from core.exact_methods.branch_and_bound import branch_and_bound_iterative
from core.graph import graph

from widgets.calculte_button import calculte_button
from widgets.upload_button import upload_button
from widgets.table_view import table_view


def run(self, weight):
    g = graph()
    array = g.read(self.fname[:len(self.fname)-4])
    tps, Benefice, capacite_prise, resultat = branch_and_bound_iterative(weight, array)

    data = {
        'Best Value': [str(Benefice)],
        'Current weight': [str(capacite_prise)],
        'Objects': [],
        'Duration': [str(tps)]
    }

    while(len(resultat) != 0):
        s = resultat.pop(len(resultat)-1)
        data['Objects'].append(
            "Objet: " + str(s.item) + " => Exemplaires: " + str(s.nbr_item))

    showResult(self, data)


def branchTab(self):

    self.main_layout = QVBoxLayout()
    welcome = QLabel('Branch and bound algorithm')
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

    upload_csv = upload_button('Upload csv file', self)
    upload_csv.setFixedWidth(120)
    upload_csv.setFixedHeight(80)

    upload_csv.clicked.connect(lambda: uploadFile(self))

    container.addWidget(maxWeight)
    container.addWidget(upload_csv)

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
        self, float(maxWeight.text())))

    calcualte.setFixedWidth(300)
    calcualte.setFixedHeight(80)

    self.main_layout.addWidget(calcualte)

    self.main_layout.addStretch(5)
    main = QWidget()
    main.setLayout(self.main_layout)
    return main


def uploadFile(self):
    fname, _ = QFileDialog.getOpenFileName(
        self, "Import CSV", "", "CSV data files (*.csv)")
    self.fname = fname


def showResult(self, data):
    self.table = table_view(data, 4, 4)
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
    header.setSectionResizeMode(1, QHeaderView.Stretch)
    header.setSectionResizeMode(2, QHeaderView.Stretch)
    header.setSectionResizeMode(3, QHeaderView.Stretch)

    self.table.setFixedWidth(1200)


    self.main_layout.addWidget(self.table)

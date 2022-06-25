from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def menu_button(name, self):
    button = QPushButton(name, self)
    button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    button.setFixedWidth(200)
    button.setFixedHeight(60)
    button.setStyleSheet("QPushButton"
                         "{"
                         "border-radius: 8px;"
                         "font-size: 14px;"
                         "text-align: left;"
                         "margin-top: 10px;"
                         "padding-left: 10px;"
                         "font-weight: medium;"
                         "background-color : #00CED1;"
                         "color: 'white';"
                         "}"

                         )
    return button

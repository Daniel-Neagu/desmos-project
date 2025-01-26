import sys
import PyQt5.QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtGui import QGuiApplication
import plot

#main frame in which we'll add the plot and the buttons and configure them and how they interact!
class MainFrame(QFrame):
    def __init__(self):
        super().__init__()

        self.setColor("black")
        self.V1 = QVBoxLayout(self)
        self.V1.addWidget(plot.graph(600,600))
        self.V2 = QVBoxLayout(self)

    #sets the background color
    def setColor(self,colour):
        self.setStyleSheet("QFrame{"
                           f"background-color: {colour};"
                           "}")
    
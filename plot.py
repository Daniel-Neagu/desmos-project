import sys
import PyQt5.QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtGui import QGuiApplication


#this is the graph which will be the largest widget in this applet
class graph(pg.PlotWidget):
    def __init__(self,min_size_x,min_size_y):
        super().__init__()
        self.setMinimumSize(min_size_x,min_size_y)
        #self.setAspectLocked() we want the graph to stretch with the entire screen so no
        self.setFocusPolicy(Qt.NoFocus)
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)

    #maybe make some functions to change the zoom levels, or tinker with other aspects 


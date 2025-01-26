import sys
import PyQt5.QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtGui import QGuiApplication
import mainframe

min_window_size_x = 900
min_window_size_y = 700

window_size_x = min_window_size_x
window_size_y = min_window_size_y

#this class just deals with the general window itself and its size and position and display, but not the contents/math involved
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #window title and sizing, and sets the window to a variable
        self.setWindowTitle("Graphing Project!!!!")
        self.resize(window_size_x,window_size_y)
        self.setMinimumHeight(min_window_size_y )
        self.setMinimumWidth(min_window_size_x)
        self.screen = QGuiApplication.primaryScreen()

        #set central widget to the frame including everything!
        self.main_frame = mainframe.MainFrame()
        self.setCentralWidget(self.main_frame)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()  # IMPORTANT!!!!! Windows are hidden by default.

    # Start the event loop.
    app.exec()

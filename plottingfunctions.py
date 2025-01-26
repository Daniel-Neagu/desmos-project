import pyqtgraph as pg
import numpy as np
from PyQt5.QtCore import Qt

def plotLine(startx,starty,endx,endy,numpoints,color,plot_graph):
    x = np.linspace(startx,endx,numpoints)
    y = np.linspace(starty,endy,numpoints)
    plot_graph.plot(x,y,pen=pg.mkPen(color,width=2))
from PyQt6 import QtWidgets, QtCore, QtGui
from pyqtgraph import plot, PlotWidget
import pyqtgraph
import sys
import random


TITLE_WINDOW: str = "Graph Window"
MIN_WIDTH: int = 500
MIN_HEIGHT: int = 300
X_VALUES: list = [random.randint(0, 100) for _ in range(10)]
Y_VALUES: list = [random.randint(0, 100) for _ in range(10)]

# sorted the values x and y
X_VALUES.sort()
Y_VALUES.sort()


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)

        # MAIN LAYOUT
        #-------------------------------------------------
        self.main_layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout()
        # remove the margin of layout
        self.main_layout.setContentsMargins(QtCore.QMargins(0, 0, 0, 0))
        #-------------------------------------------------

        # CENTRAL CONTAINER
        #-------------------------------------------------
        self.container: QtWidgets.QWidget = QtWidgets.QWidget()
        self.container.setLayout(self.main_layout)
        #-------------------------------------------------

        # loading the widgets wi
        self.create_widgets_ui()

        # loading the window
        self.create_window()
    
    def create_window(self) -> None:

        self.setWindowTitle(TITLE_WINDOW)
        self.setMinimumSize(MIN_WIDTH, MIN_HEIGHT)
        self.setCentralWidget(self.container)
        self.show()

    def create_widgets_ui(self) -> None:

        # GRAPH WIDGET
        #-------------------------------------------------
        self.graph_widget: PlotWidget = PlotWidget()

        # add lengend
        self.graph_widget.addLegend()
        
        self.graph_widget.plot(
            X_VALUES, Y_VALUES,
            name="Name here",
            pen=self.create_pen(width=2, style=QtCore.Qt.PenStyle.DotLine),
            symbol="+",
            symbolSize=20,
            symbleBrush=("b")
            )


        # change the background color
        # w = white, #FFFFFF
        self.graph_widget.setBackground("#eee")

        # title of graph
        title: str = "Title <span style='font-weight: bold;'>Here</span>"
        self.graph_widget.setTitle(title, color="#000", size="30px")


        # left an bottom labels
        style: dict = {"color":"red", "font-size":"20px"}

        self.graph_widget.setLabel("left", "Left Title", **style)
        self.graph_widget.setLabel("bottom", "Bottom Title", **style)


        # show grid of graph
        self.graph_widget.showGrid(x=True, y=True)
        #-------------------------------------------------

        # ADD WIDGETS INTO MAIN LAYOUT
        #-------------------------------------------------
        self.main_layout.addWidget(self.graph_widget)
        #-------------------------------------------------
    
    def create_pen(self, color: str = "#000", width: int | float = 1, style: QtCore.Qt.PenStyle = None) -> QtGui.QPen:
        """
        This function create a pen of graph.
        color:
            color of pen
        width:
            width of pen
        """

        return pyqtgraph.mkPen(QtGui.QColor(color), width=width, style=style)


if __name__ == "__main__":

    app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)
    window: MainWindow = MainWindow()
    sys.exit(app.exec())
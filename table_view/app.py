
from PyQt6 import QtWidgets, QtCore, QtGui
from models.model_table_view import ModelTableView
import sys
import datetime

TITLE_WINDOW: str = "TableWidget Window"
MIN_WIDTH: int = 500
MIN_HEIGHT: int = 300
DATA: list = [
    ["Hugo", 70.5, "M", datetime.datetime(2004, 2, 14).date(), True],
    ["Juliana", 45.5, "F", datetime.datetime(2007, 10, 20).date(), False],
    ["Marcos", 67.45, "M", datetime.datetime(1999, 4, 23).date(), False],
    ["Firmina", 65.2, "F", datetime.datetime(2006, 6, 10).date(), True]
]
HORIZONTAL_HEADER_LABELS: list = ["Nome", "Peso", "Sexo", "Data Nascimento", "Validado"]
VERTICAL_HEADER_LABELS: list = [1, 2, 3, 4, 5]


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)

        # MAIN LAYOUT
        #-------------------------------------------------
        self.main_layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout()
        #-------------------------------------------------

        # CENTRAL CONTAINER
        #-------------------------------------------------
        self.container: QtWidgets.QWidget = QtWidgets.QWidget()
        self.container.setLayout(self.main_layout)
        #-------------------------------------------------

        # CREATING THE WIDGETS UI
        self.create_widgets_ui()

        # the main widget of window
        self.setCentralWidget(self.container)

        # loading the settings of window
        self.create_window()
    
    def create_window(self) -> None:

        self.setWindowTitle(TITLE_WINDOW)
        self.setMinimumSize(MIN_WIDTH, MIN_HEIGHT)
        self.show()
    
    def create_widgets_ui(self) -> None:

        # LABEL TABLE
        #-------------------------------------------------
        title_lable: str = "<h1>Table <span style='color: rgba(0,0,0,0.7)'>View<\span><\h1>"
        self.label_table: QtWidgets.QLabel = QtWidgets.QLabel(title_lable)
        self.label_table.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        #-------------------------------------------------

        # TABLE VIEW
        #-------------------------------------------------
        model: ModelTableView = ModelTableView(DATA, HORIZONTAL_HEADER_LABELS, VERTICAL_HEADER_LABELS)
        self.table_view: QtWidgets.QTableView = QtWidgets.QTableView()
        self.table_view.setModel(model)

        header: QtWidgets.QHeaderView = QtWidgets.QHeaderView(QtCore.Qt.Orientation.Horizontal)
        # the last cell will occupy the rest of the window 
        header.setStretchLastSection(True)

        self.table_view.setHorizontalHeader(header)
        self.table_view.setShowGrid(False)
        self.table_view.setAlternatingRowColors(True)
        #-------------------------------------------------

        # INSERT WIDGETS UI INTO MAIN LAYOUT
        #-------------------------------------------------
        self.main_layout.addWidget(self.label_table)
        self.main_layout.addWidget(self.table_view)
        #-------------------------------------------------


if __name__ == "__main__":

    app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)
    window: MainWindow = MainWindow()
    sys.exit(app.exec())

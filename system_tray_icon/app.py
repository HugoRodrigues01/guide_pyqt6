from PyQt6 import QtWidgets, QtCore, QtGui
import sys
from tray_icon import SystemTrayIcon


TITLE_WINDOW: str = "SystemTrayIcon Window"
MIN_WIDH: int = 500
MIN_HEIGHT: int = 300


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, *kwargs)


        # MAIN LAYOUT
        #-------------------------------------------------
        self.main_layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout()
        #-------------------------------------------------

        # CENTRAL CONTAINER
        #-------------------------------------------------
        self.container: QtWidgets.QWidget = QtWidgets.QWidget()

        # add layout in central container
        self.container.setLayout(self.main_layout)
        #-------------------------------------------------


        # loading the widgets
        self.create_widgets_ui()

        # load window
        self.create_window()
    
    def create_window(self) -> None:

        self.setWindowTitle(TITLE_WINDOW)
        self.setMinimumSize(MIN_WIDH, MIN_HEIGHT)
        self.setCentralWidget(self.container)
        self.show()
    
    def create_widgets_ui(self) -> None:

        # DEPENDENCES
        #-------------------------------------------------
        self.text_label: str = \
        "<h1>Hello World!!</h1>"\
        "<p style='color: red;'>System tray icon</p>"
        #-------------------------------------------------

        # LABEL MAIN
        #-------------------------------------------------
        self.label: QtWidgets.QLabel = QtWidgets.QLabel(self.text_label)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        #-------------------------------------------------

        # INSERT WIDGETS INTO MAIN LAYOUT
        #-------------------------------------------------
        self.main_layout.addWidget(self.label)
        #-------------------------------------------------


if __name__ == "__main__":

    app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)
    window: MainWindow = MainWindow()
    # System tray icon of window
    tray_icon: SystemTrayIcon = SystemTrayIcon(window, app)
    sys.exit(app.exec())

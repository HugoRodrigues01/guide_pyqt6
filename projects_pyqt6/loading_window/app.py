from PyQt6 import QtWidgets, QtCore, QtGui
import sys


TITLE_WINDOW: str = "Loading Window"
WIDTH: int = 300
HEIGHT: int = 300


class LoadGif:
    def main(self, window: QtWidgets.QMainWindow) -> None:

        window.setObjectName("window")
        window.resize(WIDTH, HEIGHT)
        window.setStyleSheet("background-color: black;")

        # MAIN LAYOUT
        # -------------------------------------------------
        self.layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout()

        # DEFINE THE WIDGETS CONTAINER
        # -------------------------------------------------
        self.central_widgets: QtWidgets.QWidge = QtWidgets.QWidget(window)
        self.central_widgets.setObjectName("central-widgtes")
        self.central_widgets.setLayout(self.layout)

        # LABEL OF GIF
        # -------------------------------------------------
        self.label: QtWidgets.QLabel = QtWidgets.QLabel(self.central_widgets)
        self.label.setMinimumSize(WIDTH, HEIGHT)
        self.label.setMaximumSize(WIDTH, HEIGHT)
        # Resizing gif
        self.label.setScaledContents(True)

        # add label into the main layout
        self.layout.addWidget(self.label)

        window.setCentralWidget(self.central_widgets)

        self.movie: QtGui.QMovie = QtGui.QMovie("loadgif.gif")

        self.label.setMovie(self.movie)
        self.movie.start()

    def start_animation(self) -> None:
        self.movie.start()

    def stop_animation(self) -> None:
        self.movie.stop()


if __name__ == "__main__":
    app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)
    window: QtWidgets.QMainWindow = QtWidgets.QMainWindow()
    demo: LoadGif = LoadGif()
    demo.main(window)
    window.show()
    sys.exit(app.exec())

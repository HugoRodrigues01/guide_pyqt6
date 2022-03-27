from PyQt6 import QtWidgets, QtGui, QtCore
import sys


TITLE_WINDOW: str = "Widgets Window"
MIN_WIDTH: int = 500
MIN_HEIGHT: int = 300


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)

        # MAIN LAYOUT
        #-------------------------------------------------
        self.main_layout: QtWidgets.QGridLayout = QtWidgets.QGridLayout()
        #-------------------------------------------------

        # NAIN CONTAINER
        #-------------------------------------------------
        self.container: QtWidgets.QWidget = QtWidgets.QWidget()
        # insert layout in main container
        self.container.setLayout(self.main_layout)
        #-------------------------------------------------

        # load the dependences
        #-------------------------------------------------
        self.create_widgets_ui()
        #-------------------------------------------------

        # loading the window
        self.create_window()
    
    def create_window(self) -> None:

        self.setWindowTitle(TITLE_WINDOW)
        self.setCentralWidget(self.container)
        self.setMinimumSize(MIN_WIDTH, MIN_HEIGHT)
        self.show()
    
    def create_widgets_ui(self) -> None:

        style_frame: str = """
            /*
            QFrame {
                background-color: gray;
            }*/
        """

        # LABEL FRAME WIDGET
        #-------------------------------------------------
        self.label_frame_widget: QtWidgets.QLabel = QtWidgets.QLabel("Widgets")
        self.label_frame_widget.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        #-------------------------------------------------

        # FRAME WIDGETS
        #-------------------------------------------------
        self.frame_widget: QtWidgets.QFrame = QtWidgets.QFrame()
        self.frame_widget.setStyleSheet(style_frame)
        #-------------------------------------------------

        # BUTTON
        #-------------------------------------------------
        self.button: QtWidgets.QPushButton = QtWidgets.QPushButton("Press me")
        self.button.pressed.connect(lambda: self.write_plain_text("Button", "Button was pressed"))
        #-------------------------------------------------

        # SLIDER
        #-------------------------------------------------
        self.slider: QtWidgets.QSlider = QtWidgets.QSlider()

        # decoration above of slider
        self.slider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksAbove)

        # range of slider
        self.slider.setMinimum(-100)
        self.slider.setMaximum(100)

        # initial possition of slider
        self.slider.setSliderPosition(0)
        #-------------------------------------------------

        # LAYOUT FRAME WIDGETS
        #-------------------------------------------------
        self.frame_widget_layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout()

        # add layout frame widget in frame_widget
        self.frame_widget.setLayout(self.frame_widget_layout)
        #-------------------------------------------------

        # ADD WIDGETS INTO FRAME WIDGETS LAYOUT
        #-------------------------------------------------
        self.frame_widget_layout.addWidget(self.label_frame_widget)
        self.frame_widget_layout.addWidget(self.button)
        self.frame_widget_layout.addWidget(self.slider)
        #-------------------------------------------------

        # LABEL FRAME ANSWERS
        #-------------------------------------------------
        self.label_frame_answer: QtWigets.QFrame = QtWidgets.QLabel("Answers")
        self.label_frame_answer.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        #-------------------------------------------------

        # FRAME ANSWERS
        #-------------------------------------------------
        self.frame_answer: QtWidgets.QFrame = QtWidgets.QFrame()
        self.frame_answer.setMaximumWidth(400)
        self.frame_answer.setStyleSheet(style_frame)
        #-------------------------------------------------

        # PLAIN TEXT INFO
        #-------------------------------------------------
        self.text_edit_info: QtWidgets.QTextEdit = QtWidgets.QTextEdit("")
        self.text_edit_info.setStyleSheet("""
            QTextEdit {
                background-color: white;
            }
        """)
        self.text_edit_info.setReadOnly(True)
        #-------------------------------------------------  

        # BUTTON CLEAR
        #-------------------------------------------------
        self.button_clear: QtWidgets.QPushButton = QtWidgets.QPushButton("Clear")
        self.button_clear.pressed.connect(self.text_edit_info.clear)
        #-------------------------------------------------

        # LAYOUT FRAME ANSWERS
        #-------------------------------------------------
        self.frame_answer_layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout()

        # add frame answers layout in frame answers
        self.frame_answer.setLayout(self.frame_answer_layout)
        #-------------------------------------------------

        # ADD WIDGETS INTO FRAME ANSWERS LAYOUT
        #-------------------------------------------------
        self.frame_answer_layout.addWidget(self.label_frame_answer)
        self.frame_answer_layout.addWidget(self.text_edit_info)
        self.frame_answer_layout.addWidget(self.button_clear)
        #-------------------------------------------------

        # ADD WIDGETS INTO THE MAIN LAYOUT
        #-------------------------------------------------
        self.main_layout.addWidget(self.frame_widget, 0, 0)
        self.main_layout.addWidget(self.frame_answer, 0, 1)
        #-------------------------------------------------
    
    def write_plain_text(self, title: str, text: str) -> None:

        self.text_edit_info.append("-" * 70)
        self.text_edit_info.append(f"<span style='color: red;'>{title}</span> <br> {text}")
        self.text_edit_info.append("-" * 70)


if __name__ == "__main__":

    app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)
    window: MainWindow = MainWindow()
    sys.exit(app.exec())

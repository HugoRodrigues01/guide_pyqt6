from PyQt6 import QtWidgets, QtCore, QtGui
import sys, traceback
import time
from rich.console import Console
from typing import Any

console: Console = Console()


class WorkerSignals(QtCore.QObject):

    finished = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal(tuple)
    result = QtCore.pyqtSignal(object)
    progress = QtCore.pyqtSignal(int)


class Worker(QtCore.QRunnable):
    def __init__(self, function: Any, *args, **kwargs) -> None:
        super(Worker, self).__init__()

        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        # self.kwargs["progress_callback"] = self.signals.progress

    @QtCore.pyqtSlot()
    def run(self) -> None:
        """
        Initialise your function.
        """

        try:
            result = self.function(*self.args, **self.kwargs)

        except Exception as error:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))

        else:
            self.signals.result.emit(result)  # Return the result of the processing

        finally:
            self.signals.finished.emit()  # Done


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)

        # THREAD POOL
        self.thread_pool: QtCore.QThreadPool = QtCore.QThreadPool()
        console.log(f"Maximum thread count {self.thread_pool.maxThreadCount()}")

        self._count: int = 0

        # MAIN LAYOUT
        self.main_layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout()

        # MAIN CONTAINER
        self.main_container: QtWidgets.QWidget = QtWidgets.QWidget()
        self.main_container.setLayout(self.main_layout)

        # LABEL MAIN
        # label of time
        self.label: QtWidgets.QLabel = QtWidgets.QLabel("0")

        # BUTTON START PROCESS
        self.button: Qtwidgets.QPushButton = QtWidgets.QPushButton("START")
        self.button.pressed.connect(self.start_worker)

        # ADD THE WIDGETS INTO THE MAIN LYOUT
        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.button)

        # TIMER
        self.timer: QtCore.QTimer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.start_timer)
        self.timer.start()

        # SETTINGS OF WINDOW
        self.setCentralWidget(self.main_container)
        self.setMinimumSize(400, 100)
        self.setWindowTitle("Threads")
        self.show()

    def progress_function(self, proces) -> None:
        console.log(f"{process}")

    def print_output(self, output) -> None:
        console.log("Output ", output)

    def start_process(self) -> None:
        console.log("start process")
        time.sleep(4)
        console.log("finish process")

    def start_worker(self) -> None:
        # Pass the function to execute
        worker: Worker = Worker(self.start_process)
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(lambda: print("FINISHED THREAD"))
        worker.signals.progress.connect(self.progress_function)

        self.thread_pool.start(worker)

    def start_timer(self) -> None:
        self._count += 1
        self.label.setText(str(self._count))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window: MainWindow = MainWindow()
    sys.exit(app.exec())

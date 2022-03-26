from PyQt6 import QtWidgets, QtCore, QtGui
import os

# ATENTION!!, the images or icons of code just loaded, if run of python code
# was in guide_pyqt6 directory

# (venv) zero-two@zerotwo:~/Documentos/python-pyqt/guide_pyqt6$ python pyqt6/dir_widget_name/app.py
ICONS_PATH: str = os.curdir + "/icons"


class SystemTrayIcon:

    def __init__(self, perent, application: QtWidgets.QApplication, *args, **kwargs) -> None:
        
        self.__perent = perent
        self.__app: QtWidgets.QApplication = application
        self.__app.setQuitOnLastWindowClosed(False)

        self.icon: QtGui.QIcon = QtGui.QIcon(ICONS_PATH + "/computador(2).png")

        # icon of tray icon
        self.tray: QtWidgets.QSystemTrayIcon = QtWidgets.QSystemTrayIcon(self.__perent)
        self.tray.setIcon(self.icon)
        self.tray.setVisible(True)

        # loading the menu
        self.create_menu()

        # insert menu into system tray icon
        self.tray.setContextMenu(self.menu)


    def create_menu(self) -> None:

        # loading the actions
        self.create_actions()

        #  MENU
        #-------------------------------------------------
        self.menu = QtWidgets.QMenu("Menu tray icon")

        # Add action into menu
        self.menu.addAction(self.action_show_hide)
        self.menu.addSeparator()
        self.menu.addAction(self.action_quit_window)
        #-------------------------------------------------

    def create_actions(self) -> None:

        # ACTION QUIT WINDOW
        #-------------------------------------------------
        self.action_quit_window: QtGui.QAction = QtGui.QAction(QtGui.QIcon(ICONS_PATH + "/botao-de-menos.png"), "Quit")
        self.action_quit_window.triggered.connect(self.__app.quit)
        #-------------------------------------------------

        # ACTION SHOW/HIDDEN WINDOW
        #-------------------------------------------------
        self.action_show_hide: QtGui.QAction = QtGui.QAction("Show/Hide")
        self.action_show_hide.triggered.connect(self.show_hide_function)
        #-------------------------------------------------
    
    def show_hide_function(self) -> None:
        """
        This function will verify if the main window is visible, if not, the window will be hide
        """

        if self.__perent.isVisible():
            self.__perent.hide()
        
        elif self.__perent.isVisible() == False:
            self.__perent.show()

from PyQt6 import QtWidgets, QtCore, QtGui
import datetime

ICONS_PATH: str = "../icons"


class ModelTableView(QtCore.QAbstractTableModel):

    def __init__(self, data: list = [], horizontal_header: list = [], vertical_header: list = [], *args, **kwargs) -> None:
        super(ModelTableView, self).__init__(*args, **kwargs)

        self._data: list = data

        #-------------------------------------------------
        self._horizontal_header: list = horizontal_header

        if len(self._horizontal_header ) == 0:
            self._horizontal_header = [index for index in range(len(self._data[0]))] 
        #-------------------------------------------------
        #-------------------------------------------------
        self._vertical_header: list = vertical_header

        if len(self._vertical_header) == 0:
            self._vertical_header = [index for index in range(len(self._data))]
        #-------------------------------------------------
    
    def data(self, index, role):

        data: list = self._data[index.row()][index.column()]

        # Return the string of data
        if role == QtCore.Qt.ItemDataRole.DisplayRole:

            if isinstance(data, datetime.date):
                # return data formating for date brazil
                return str(data.strftime("%d/%m/%Y"))

            return str(data)


    def rowCount(self, index = ...) -> int:
        return len(self._data)
    
    def columnCount(self, index = ...) -> int:
        return len(self._data[0])

    def headerData(self, section, orientation, role) -> str: 

        # section: index of column/row
        if role == QtCore.Qt.ItemDataRole.DisplayRole:

            if orientation == QtCore.Qt.Orientation.Horizontal:
                return str(self._horizontal_header[section])
            
            if orientation == QtCore.Qt.Orientation.Vertical:
                return str(self._vertical_header[section])
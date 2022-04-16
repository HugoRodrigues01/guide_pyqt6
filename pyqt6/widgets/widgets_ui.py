from PyQt6 import QtWidgets, QtGui, QtCore


class WidgetsUIWidgets:

    def __init__(self, container, perent, infos_area) -> None:

        self.perent = perent or None
        self.infos_area = infos_area or None
    
        # MAIN LAYOUT
        #-------------------------------------------------
        self.main_layout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout()
        #-------------------------------------------------

        container.setLayout(self.main_layout)

    def create_widgets_ui(self) -> None:

        # SPIN BOX
        #-------------------------------------------------
        self.spin_box: QtWidgets.QSpinBox = QtWidgets.QSpinBox()
        
        self.spin_box.valueChanged.connect(lambda info: self.infos_area("Spin Box", f"Text Changed: {info}"))
        #-------------------------------------------------

        # SLIDER
        #-------------------------------------------------
        self.slider: QtWidgets.QSlider = QtWidgets.QSlider()

        # size
        self.slider.setMinimumHeight(100)

        # decoration above of slider
        self.slider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksAbove)

        # range of slider
        self.slider.setMinimum(-100)
        self.slider.setMaximum(100)

        # initial possition of slider
        self.slider.setSliderPosition(0)

        self.slider.valueChanged.connect(lambda info: self.infos_area("Slider", f"Value Changed: {info}"))
        #-------------------------------------------------

        # RADIO BUTTON
        #-------------------------------------------------
        self.radio_button: QtWidgets.QRadioButton = QtWidgets.QRadioButton("Radio Button")
        #-------------------------------------------------

        # DATETIME
        #-------------------------------------------------
        self.datetime: QtWidgets.QDateTimeEdit = QtWidgets.QDateTimeEdit()
        #-------------------------------------------------

        # CHECKBOX 
        #-------------------------------------------------
        self.checkbox: QtWidgets.QCheckBox = QtWidgets.QCheckBox("Check box")
        #-------------------------------------------------

        # ADD WIDGETS INTO THE MAIN LAYOUT
        #-------------------------------------------------

        self.main_layout.addWidget(self.spin_box)
        self.main_layout.addWidget(self.slider)
        self.main_layout.addWidget(self.radio_button)
        self.main_layout.addWidget(self.datetime)
        self.main_layout.addWidget(self.checkbox)
        #-------------------------------------------------

from PyQt4.QtGui import *
import sys

class RadioButton(QWidget):
    def __init__(self, label, button_list):
        super().__init__()

        self.title_label = QLabel(label)
        self.radio_group_box = QGroupBox()
        self.radio_button_group = QButtonGroup()

        self.radio_button_list = []

        for button in button_list:
            self.radio_button_list.append(QRadioButton(button))

        self.radio_button_list[0].setChecked(True)

        self.radio_button_layout = QVBoxLayout()

        counter = 1

        for button in self.radio_button_list:
            self.radio_button_layout.addWidget(button)
            self.radio_button_group.addButton(button)
            self.radio_button_group.setId(button, counter)

            counter += 1

        self.radio_group_box.setLayout(self.radio_button_layout)

        self.main_radio_button_layout = QVBoxLayout()
        self.main_radio_button_layout.addWidget(self.title_label)
        self.main_radio_button_layout.addWidget(self.radio_group_box)
        self.setLayout(self.main_radio_button_layout)

    def selected_button(self):
        return self.radio_button_group.checkedId()

    def check_first(self):
        self.radio_button_list[0].setChecked(True)
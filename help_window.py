from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QVBoxLayout, QStackedLayout, QWidget
from PyQt5.QtCore import Qt


class HelpWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Help')
        self.setGeometry(600, 150, 500, 400)

        self.widget1 = QWidget()
        self.layout1 = QVBoxLayout()
        self.widget1.setLayout(self.layout1)
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.widget1)
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)
        self.rules_grid = QGridLayout()

        self.label1 = QLabel('Oczko - 21')
        self.label1.setAlignment(Qt.AlignCenter|Qt.AlignTop)

        self.label2 = QLabel('Rules of the game:\n\n\n\n'
                             '1. Collect points based on card\'s figure. Pull cards from the deck or stop the card.\n\n'
                             '2. If you exceed 21 points, you loose. One and only exception is when you pull two aces in the row (22 points).\n\n'
                             '3. If none of players has got 21 and both stop the card, the winner is with bigger score.\n\n'
                             '4. If both of them have the same amount of points there is a draw.\n\n'
                             '5. If both players stop pulling the card, one after another, this means game is over\n\n'
                             '6. There are 9 turns - \'deals\'. Player with higher score, wins.')

        self.label3 = QLabel('Created by D.G. 2018')
        self.label3.setAlignment(Qt.AlignRight|Qt.AlignBottom)

        self.rules_grid.addWidget(self.label1, 0, 0)
        self.rules_grid.addWidget(self.label2,1,0)
        self.rules_grid.addWidget(self.label3, 2, 0)

        self.layout1.addLayout(self.rules_grid)
        self.label1.move(100,100)
        # self.welcome_layout.addWidget(self.btn)




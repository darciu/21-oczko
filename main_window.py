import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import time
import random

from help_window import *
from radio_button_class import *
from deck import *

class mainWindow(QMainWindow):
    end_game = False

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Oczko 21')
        self.setGeometry(400,60,700,650)
        self.create_welcome_layout()
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.welcome_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)

        #====================Create New Game Layout=====================
        self.create_new_game_layout()
        self.stacked_layout.addWidget(self.new_game_widget)


        #==========================MAIN MENU====================================
        self.statusBar()
        newGame = QAction('&New Game', self)
        newGame.setStatusTip('Starts a new game...')
        newGame.triggered.connect(self.newGame_opt)

        help = QAction('&Help', self)
        help.setStatusTip('Help...')
        help.triggered.connect(self.help_opt)

        quitGame = QAction('&Quit', self)
        quitGame.setStatusTip('Quits the game...')
        quitGame.triggered.connect(self.quit_opt)

        mainMenu = self.menuBar()

        optionsMenu = mainMenu.addMenu('&Options')
        optionsMenu.addAction(newGame)
        optionsMenu.addAction(help)
        optionsMenu.addAction(quitGame)

        #=======================END MAIN MENU===========================================

    def newGame_opt(self):      #options from menu bar

        if self.stacked_layout.currentIndex() != 0:
            choice = QMessageBox.question(self, 'Start a new game', 'Do you want to start a new game?',
                                          QMessageBox.Yes | QMessageBox.No)

            if choice == QMessageBox.Yes:
                self.new_game_radio_button.check_first()
                self.stacked_layout.setCurrentIndex(1)
                self.player1_line_edit.setText('Player 1')
                self.player2_line_edit.setText('Player 2')
            else:
                pass

        else:
            self.new_game_radio_button.check_first()
            self.stacked_layout.setCurrentIndex(1)
            self.player1_line_edit.setText('Player 1')
            self.player2_line_edit.setText('Player 2')


    def quit_opt(self):     #options from menu bar

        choice = QMessageBox.question(self,'Exit','Do you really want to exit the game?',QMessageBox.Yes|QMessageBox.No)

        if choice == QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def help_opt(self):     # options from menu bar

        self.dialog = HelpWindow()
        self.dialog.show()

    @classmethod
    def end_game_change_value(cls,value):       #method used to verify if game has ended
        cls.end_game = value



    def create_welcome_layout(self):        #first layout


        self.welcome_layout = QVBoxLayout()
        self.welcome_widget = QWidget()
        self.welcome_widget.setLayout(self.welcome_layout)


    def create_new_game_layout(self):      #start new game layout (new game menu)

        self.player1_label = QLabel('First player name:')
        self.player2_label = QLabel('Second player name:')

        self.player1_line_edit = QLineEdit()
        self.player2_line_edit = QLineEdit()



        self.cancel_button = QPushButton('Cancel')
        self.start_button = QPushButton('Start New Game')

        self.start_button.clicked.connect(self.start_new_game)
        self.cancel_button.clicked.connect(self.cancel)

        self.player_grid = QGridLayout()
        self.new_game_grid = QGridLayout()

        #player grid
        self.player_grid.addWidget(self.player1_label,0,0)
        self.player_grid.addWidget(self.player2_label, 1, 0)
        self.player_grid.addWidget(self.player1_line_edit, 0, 1)
        self.player_grid.addWidget(self.player2_line_edit, 1, 1)


        #new game grid

        self.new_game_radio_button = RadioButton('Play with',('NPC','Friend'))
        self.new_game_grid.addWidget(self.new_game_radio_button,0,0)
        self.new_game_grid.addLayout(self.player_grid,0,1)
        self.new_game_grid.addWidget(self.cancel_button,1,0)
        self.new_game_grid.addWidget(self.start_button, 1, 1)


        self.new_game_widget = QWidget()
        self.new_game_widget.setLayout(self.new_game_grid)



    def create_game_layout(self, player_type):

        self.player1_points = QLabel('0')
        self.player2_points = QLabel('0')

        self.player1_name = QLabel(self.player1_line_edit.text())

        if player_type == 1:
            self.player2_name = QLabel(self.player2_line_edit.text() + ' (NPC)')
        else:
            self.player2_name = QLabel(self.player2_line_edit.text())


        self.points1_label = QLabel('Points:')
        self.points2_label = QLabel('Points:')

        self.player1_card = QLabel()
        self.player2_card = QLabel()

        self.stop_button_player1 = QPushButton('Stop')
        self.pull_button_player1 = QPushButton('Pull')

        self.stop_button_player2 = QPushButton('Stop')
        self.pull_button_player2 = QPushButton('Pull')

        self.new_deal_button = QPushButton('New Deal')
        self.information_field = QPlainTextEdit('Log here baby')

        self.table = QTableWidget()
        self.table.setRowCount(10)
        self.table.setColumnCount(2)


        #Buttons connection
        self.stop_button_player1.clicked.connect(lambda: self.stop_card_player1(player_type))
        self.pull_button_player1.clicked.connect(lambda: self.pull_card_player1(player_type))

        self.stop_button_player2.clicked.connect(self.stop_card_player2)
        self.pull_button_player2.clicked.connect(self.pull_card_player2)

        self.new_deal_button.clicked.connect(self.new_deal)

        #Table

        self.table = QTableWidget()
        self.table.setRowCount(11)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(("{0};{1};").format(self.player1_name.text(),self.player2_name.text()).split(";"))
        self.table.setVerticalHeaderLabels(("1;2;3;4;5;6;7;8;9;10;SUM").split(";"))

        #Grids definitions

        self.main_game_grid = QGridLayout()
        self.board_grid = QGridLayout()
        self.table_grid = QGridLayout()
        self.below_table_grid = QGridLayout()

        self.player1_grid = QGridLayout()
        self.player2_grid = QGridLayout()

        self.player1_board_grid = QGridLayout()
        self.player2_board_grid = QGridLayout()

        self.player1_buttons_grid = QGridLayout()
        self.player2_buttons_grid = QGridLayout()

        self.player1_points_grid = QGridLayout()
        self.player2_points_grid = QGridLayout()


        #player points grids

        self.player1_points_grid.addWidget(self.points1_label,0,0)
        self.player1_points_grid.addWidget(self.player1_points, 1, 0)

        self.player2_points_grid.addWidget(self.points2_label, 0, 0)
        self.player2_points_grid.addWidget(self.player2_points, 1, 0)

        #player buttons grids

        self.player1_buttons_grid.addWidget(self.stop_button_player1,0,0)
        self.player1_buttons_grid.addWidget(self.pull_button_player1, 0, 1)

        self.player2_buttons_grid.addWidget(self.stop_button_player2, 0, 0)
        self.player2_buttons_grid.addWidget(self.pull_button_player2, 0, 1)

        #player board grids

        self.player1_board_grid.addWidget(self.player1_name,0,0)
        self.player1_board_grid.addWidget(self.player1_card, 0, 1)
        self.player1_board_grid.addLayout(self.player1_points_grid,0,3)

        self.player2_board_grid.addWidget(self.player2_name, 0, 0)
        self.player2_board_grid.addWidget(self.player2_card, 0, 1)
        self.player2_board_grid.addLayout(self.player2_points_grid, 0, 3)

        #player grids

        self.player1_grid.addLayout(self.player1_buttons_grid,0,0)
        self.player1_grid.addLayout(self.player1_board_grid, 1, 0)

        self.player2_grid.addLayout(self.player2_buttons_grid, 1, 0)
        self.player2_grid.addLayout(self.player2_board_grid, 0, 0)


        #below table grid

        self.below_table_grid.addWidget(self.information_field,0,0)
        self.below_table_grid.addWidget(self.new_deal_button, 0, 1)

        #three main grids

        self.board_grid.addLayout(self.player1_grid,0,0)
        self.board_grid.addLayout(self.player2_grid, 1, 0)

        self.table_grid.addWidget(self.table, 0, 0)
        self.table_grid.addLayout(self.below_table_grid,1,0)

        self.main_game_grid.addLayout(self.board_grid,0,0)
        self.main_game_grid.addLayout(self.table_grid, 0, 1)

        # layout

        self.game_widget = QWidget()
        self.game_widget.setLayout(self.main_game_grid)


    def cancel(self):

        self.stacked_layout.setCurrentIndex(0)
        self.textbox.setText('0')

    def start_new_game(self):

        player_type = self.new_game_radio_button.selected_button()

        if len(self.player1_line_edit.text()) > 10 or len(self.player2_line_edit.text()) > 10:
            QMessageBox.information(self, "Too long name","At least one of player's name is too long. It has to be shorter than 10 characters.")




        elif self.player1_line_edit.text() == '' or self.player2_line_edit.text() == '':
            QMessageBox.information(self, "Empty name", "At least one of player's name is empty. Please provide correct one.")

        else:
            if self.stacked_layout.count() > 2:
                self.stacked_layout.removeWidget(self.game_widget)

            self.create_game_layout(player_type)
            self.stacked_layout.addWidget(self.game_widget)
            self.stacked_layout.setCurrentIndex(2)
            self.player1_score = 0
            self.player2_score = 0
            self.match = -1
            self.new_match()

    def new_match(self):
        self.end_game_change_value(False)
        self.new_deal_button.setDisabled(True)
        self.match +=1
        self.deck = Deck()
        self.turn = 0
        self.disable_player2_buttons()
        self.stop_counter = 0
        self.player1_allcards = []
        self.player2_allcards = []
        self.pixmap = QPixmap('karty\empty.png')
        self.pixmap = self.pixmap.scaledToWidth(180)
        self.player1_card.setPixmap(self.pixmap)
        self.player2_card.setPixmap(self.pixmap)
        self.information_field.setPlainText('New deal! {0} starts'.format(self.player1_name.text()))


    def pull_card_player1(self,player_type):
        #card pixmap
        self.pixmap1 = QPixmap('karty\{0}.png'.format(self.deck.pack[self.turn]))
        self.pixmap1 = self.pixmap1.scaledToWidth(180)
        self.player1_card.setPixmap(self.pixmap1)

        self.player1_points.setText(str(int(self.player1_points.text()) + self.points(self.deck.pack[self.turn][:2])))
        #log info
        self.information_field.setPlainText(self.information_field.toPlainText() + '\n{0} pulls and gains {1} points'.format(self.player1_name.text(),str(self.points(self.deck.pack[self.turn][:2]))))


        self.player1_allcards.append(self.deck.pack[self.turn])

        self.turn += 1
        self.stop_counter = 0
        self.disable_player1_buttons()
        if player_type == 1:
            self.game_function()
            if self.end_game == False:
                self.npc_turn()
        elif player_type == 2 and self.end_game == False:
            self.enable_player2_buttons()
            self.game_function()
        else:
            self.disable_player1_buttons()
            self.disable_player2_buttons()




    def stop_card_player1(self,player_type):

        self.stop_counter += 1
        #log info
        self.information_field.setPlainText(self.information_field.toPlainText() + '\n{0} stops the card'.format(self.player1_name.text()))

        self.disable_player1_buttons()

        if player_type == 1:
            self.game_function()
            if self.end_game == False:
                self.npc_turn()
        elif player_type == 2 and self.end_game == False:
            self.enable_player2_buttons()
            self.game_function()
        else:
            self.disable_player1_buttons()
            self.disable_player2_buttons()

    def pull_card_player2(self):
        #card pixmap
        self.pixmap2 = QPixmap('karty\{0}.png'.format(self.deck.pack[self.turn]))
        self.pixmap2 = self.pixmap2.scaledToWidth(180)
        self.player2_card.setPixmap(self.pixmap2)

        self.player2_points.setText(str(int(self.player2_points.text()) + self.points(self.deck.pack[self.turn][:2])))

        #log info
        self.information_field.setPlainText(self.information_field.toPlainText() + '\n{0} pulls and gains {1} points'.format(self.player2_name.text(), str(self.points(self.deck.pack[self.turn][:2]))) )

        self.player2_allcards.append(self.deck.pack[self.turn])

        self.turn += 1
        self.stop_counter = 0
        self.disable_player2_buttons()

        if self.end_game == False:
            self.enable_player1_buttons()
            self.game_function()
        else:
            self.disable_player1_buttons()



    def stop_card_player2(self):

        self.disable_player2_buttons()
        self.stop_counter += 1
        #log info
        self.information_field.setPlainText(self.information_field.toPlainText() + '\n{0} stops the card'.format(self.player2_name.text()))

        if self.end_game == False:
            self.enable_player1_buttons()
            self.game_function()



    def game_function(self):       #check whether there is a winning result

        if int(self.player1_points.text()) == 21 and int(self.player2_points.text()) == 21:
            self.draw()

        if int(self.player1_points.text()) == 21 and self.stop_counter == 1:
            self.player1_wins()

        if int(self.player2_points.text()) == 21 and self.stop_counter == 1:
            self.player2_wins()

        # =====================Two Aces========================

        if int(self.player1_points.text()) == 22 and 'AA' in self.player1_allcards[0] and 'AA' in self.player1_allcards[1]:
            self.player1_wins()
            self.information_field.setPlainText(self.information_field.toPlainText() + '\n{0} has two Aces!'.format(self.player1_name.text()))



        if int(self.player2_points.text()) == 22 and 'AA' in self.player2_allcards[0] and 'AA' in self.player2_allcards[1]:
            self.player2_wins()
            self.information_field.setPlainText(self.information_field.toPlainText() + '\n{0} has two Aces!'.format(self.player1_name.text()))

        # ==================================================================

        #============================Two times Stop button in row============================

        if self.stop_counter == 2:
            if int(self.player1_points.text()) > int(self.player2_points.text()):
                self.player1_wins()

            elif int(self.player1_points.text()) < int(self.player2_points.text()):
                self.player2_wins()

            else:
                self.draw()


        if int(self.player1_points.text()) > 21:    # player 1 exceeds 21 points
            self.information_field.setPlainText(self.information_field.toPlainText() + '. 21 is exceeded!')
            self.player2_wins()

        if int(self.player2_points.text()) > 21:    # player 2 exceeds 21 points
            self.disable_player1_buttons()
            self.information_field.setPlainText(self.information_field.toPlainText() + '. 21 is exceeded!')
            self.player1_wins()

    def npc_turn(self):     #determines when npc pulls or stops the card
        time.sleep(0.5)
        if int(self.player1_points.text()) == 21 and int(self.player2_points.text()) in [18,19]:
            self.pull_card_player2()
        elif int(self.player1_points.text()) == 21 and int(self.player2_points.text()) == 20:
            self.stop_card_player2()
        elif int(self.player1_points.text()) >= 21:
            self.stop_card_player2()
        elif int(self.player1_points.text()) >= int(self.player2_points.text()) or int(self.player2_points.text()) <= 11:
            self.pull_card_player2()
        elif int(self.player2_points.text()) == 12:
            if random.randint(0,100) < 85:
                self.pull_card_player2()
            else:
                self.stop_card_player2()
        elif int(self.player2_points.text()) == 13:
            if random.randint(0,100) < 80:
                self.pull_card_player2()
            else:
                self.stop_card_player2()
        elif int(self.player2_points.text()) == 14:
            if random.randint(0,100) < 70:
                self.pull_card_player2()
            else:
                self.stop_card_player2()
        elif int(self.player2_points.text()) == 15:
            if random.randint(0,100) < 50:
                self.pull_card_player2()
            else:
                self.stop_card_player2()
        elif int(self.player2_points.text()) == 16:
            if random.randint(0,100) < 35:
                self.pull_card_player2()
            else:
                self.stop_card_player2()
        elif int(self.player2_points.text()) == 17:
            if random.randint(0,100) < 20:
                self.pull_card_player2()
            else:
                self.stop_card_player2()
        elif int(self.player2_points.text()) >= 18:
            if random.randint(0, 100) < 5:
                self.pull_card_player2()
            else:
                self.stop_card_player2()
        else:
            self.stop_card_player2()



    def player1_wins(self):    #action when player 1 wins
        self.player1_score +=1
        self.sum_rows()
        self.disable_player1_buttons()
        self.disable_player2_buttons()
        self.table.setItem(self.match, 0, QTableWidgetItem('1'))
        self.table.setItem(self.match, 1, QTableWidgetItem('0'))
        self.end_game_change_value(True)
        #log
        self.information_field.setPlainText(self.information_field.toPlainText() + '\n{0} wins the deal with {1} points!'.format(self.player1_name.text(), self.player1_points.text()))
        if self.match < 9:
            self.new_deal_button.setDisabled(False)
        else:
            self.result_message(self.player1_score,self.player2_score)

    def player2_wins(self):     #action when player 2 wins
        self.player2_score +=1
        self.sum_rows()
        self.disable_player1_buttons()
        self.disable_player2_buttons()
        self.table.setItem(self.match, 0, QTableWidgetItem('0'))
        self.table.setItem(self.match, 1, QTableWidgetItem('1'))
        self.end_game_change_value(True)
        #log
        self.information_field.setPlainText(self.information_field.toPlainText() + '\n{0} wins the deal with {1} points!'.format(self.player2_name.text(),self.player2_points.text()))
        if self.match < 9:
            self.new_deal_button.setDisabled(False)
        else:
            self.result_message(self.player1_score, self.player2_score)

    def draw(self):     #action when there is a draw
        self.disable_player1_buttons()
        self.disable_player2_buttons()
        self.table.setItem(self.match, 0, QTableWidgetItem('0'))
        self.table.setItem(self.match, 1, QTableWidgetItem('0'))
        self.end_game_change_value(True)
        #log
        self.information_field.setPlainText(self.information_field.toPlainText() + '\nDraw!')
        if self.match < 9:
            self.new_deal_button.setDisabled(False)
        else:
            self.result_message(self.player1_score, self.player2_score)

    def result_message(self,player1_score,player2_score):
        if player1_score > player2_score:
            QMessageBox.information(self, "{0} won!".format(self.player1_name.text()), "The score is {0}:{1}. Good luck next time {2}!".format(player1_score,player2_score,self.player2_name.text()))
        elif player1_score < player2_score:
            QMessageBox.information(self, "{0} won!".format(self.player2_name.text()),"The score is {0}:{1}. Good luck next time {2}!".format(player2_score, player1_score, self.player1_name.text()))
        else:
            QMessageBox.information(self, "Draw!", "Both players scored {0} points".format(player1_score))


    def disable_player1_buttons(self):
        self.pull_button_player1.setDisabled(True)
        self.stop_button_player1.setDisabled(True)

    def enable_player1_buttons(self):
        self.pull_button_player1.setDisabled(False)
        self.stop_button_player1.setDisabled(False)

    def disable_player2_buttons(self):
        self.pull_button_player2.setDisabled(True)
        self.stop_button_player2.setDisabled(True)

    def enable_player2_buttons(self):
        self.pull_button_player2.setDisabled(False)
        self.stop_button_player2.setDisabled(False)

    def points(self,value):     #method to match card's name with its points value
        score = {'11':1,'22':2,'33':3,'44':4,'55':5,'66':6,'77':7,'88':8,'99':9,'10':10,'WW':2,'DD':3,'KK':4,'AA':11}
        return score[value]


    def sum_rows(self):     #sums rows from the table
        self.table.setItem(10, 0, QTableWidgetItem(str(self.player1_score)))
        self.table.setItem(10, 1, QTableWidgetItem(str(self.player2_score)))

    def new_deal(self):     #start new deal

        self.enable_player1_buttons()
        self.player1_card.setText('')
        self.player2_card.setText('')
        self.player1_points.setText('0')
        self.player2_points.setText('0')
        self.new_match()


def main():
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    window.raise_()
    app.exec()

if __name__ == '__main__':
    main()
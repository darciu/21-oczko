import random

class Deck():
    def __init__(self):
        self.cards = ['22', '33', '44', '55', '66', '77', '88', '99', '10', 'WW', 'DD', 'KK', 'AA']
        self.pack = []

        for i in range(len(self.cards)):
            self.pack.append(self.cards[i] + ' Kier')
            self.pack.append(self.cards[i] + ' Pik')
            self.pack.append(self.cards[i] + ' Trefl')
            self.pack.append(self.cards[i] + ' Karo')

        random.shuffle(self.pack)

    def points(self,value):
        if value[:1] == '22':
            return 2
        elif value[:1] == '33':
            return 3
        elif value[:1] == '44':
            return 4
        elif value[:1] == '55':
            return 5
        elif value[:1] == '66':
            return 6
        elif value[:1] == '77':
            return 7
        elif value[:1] == '88':
            return 8
        elif value[:1] == '99':
            return 9
        elif value[:1] == '10':
            return 10
        elif value[:1] == 'WW':
            return 2
        elif value[:1] == 'DD':
            return 3
        elif value[:1] == 'KK':
            return 4
        elif value[:1] == 'AA':
            return 11
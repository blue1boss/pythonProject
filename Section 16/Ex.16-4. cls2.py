class HoldemPlayer:
    card 3 = ''
    card 4 = ''
    card 3 = ''
    card 3 = ''


    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2

    def get_card_info(self):
        print(f'card1:{self.card1}')
        print(f'card2:{self.card2}')
        print(f'card3:{self.card3}')
        print(f'card4:{self.card4}')
        #7까지 classmethod도 같이 하기
    @classmethod
    def set_card3(cls,card):
        cls.card3 = card

    @classmethod
    def set_card4(cls, card):
        cls.card4 = card

    @classmethod
    def set_card5(cls, card):
        cls.card5 = card

#실행
player1= HoldemPlayer('S-A','S-K')
player2= HoldemPlayer('D-2','D-7')
player3= HoldemPlayer('H-A','C-4')

print('1Round')
print('player1')
player1.get_card_info()
print('player2')
player2.get_card_info()

print(f'player1 {player1.get_card_info()}')
print(f'player2 {player2.get_card_info()}')
print(f'player3 {player3.get_card_info()}')
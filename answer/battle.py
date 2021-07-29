import random

from player import Player
from const import HAND 

class Battle():
    '''
    ジャンケンの試合を管理
    '''
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.player1_hand = None
        self.player2_hand = None
        self.result = {} # {player.name: result} 

    def start(self):
        '''
        試合開始
        '''
        self.player1_hand = self.hand_random()
        self.player2_hand = self.hand_random()

    def hand_random(self):
        '''
        ランダムに手を選択
        '''
        return random.randint(0, 2)

    def judge_winer(self):
        '''
        結果を判定する
        '''
        print(f"{self.player1.name}:{HAND.HAND_NAME[self.player1_hand]}")
        print(f"{self.player2.name}:{HAND.HAND_NAME[self.player2_hand]}")
        # あいこ
        if self.player1_hand == self.player2_hand:
            self.result[self.player1.name] = "draw"
            self.result[self.player2.name] = "draw"
            self.player1.draw_count += 1
            self.player2.draw_count += 1
            print("あいこ　です")
        # Player1 の勝ち
        elif self.player1_hand == HAND.GUU and self.player2_hand == HAND.TYOKI or\
             self.player1_hand == HAND.TYOKI and self.player2_hand == HAND.PAA or\
             self.player1_hand == HAND.PAA and self.player2_hand == HAND.GUU:
            self.result[self.player1.name] = "win"
            self.result[self.player2.name] = "lose"
            self.player1.win_count += 1
            self.player2.lose_count += 1
            print(f"{self.player1.name} の　勝ち　です。")
        # Player2 の勝ち
        else:
            self.result[self.player1.name] = "lose"
            self.result[self.player2.name] = "win"
            self.player1.lose_count += 1
            self.player2.win_count += 1
            print(f"{self.player2.name} の　勝ち　です。")
        print("=================================")
        
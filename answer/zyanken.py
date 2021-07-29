import random
import pprint

from battle import Battle
from player import Player

class Zyanken():
    '''
    ジャンケン全体を管理
    '''
    def __init__(self):
        self.player_list: list[Player] = [] # listの内部の型を指定できる
        self.battle_record: list[Battle] = []

    def register_player(self, player: Player):
        '''
        プレイヤーを追加
        '''
        self.player_list.append(player)

    def show_all_players(self):
        '''
        全てのプレイヤー情報を表示
        '''
        for player in self.player_list:
            print(player.__dict__) # 簡単に全情報を出力したい場合は__dict__を用いる
            
    def show_battle_record(self):
        '''
        試合の履歴を表示
        '''
        for r in self.battle_record:
            for k, v in r.__dict__.items():
                try:
                    print({k: r.__dict__[k].__dict__})
                except:
                    print({k: r.__dict__[k]})
            print("=================================")

    def match_random(self):
        '''
        プレイヤーをランダムに選択する
        '''
        player1_index = 0
        player2_index = 0
        while player1_index == player2_index:
            player1_index = random.randint(0, len(self.player_list)-1)
            player2_index = random.randint(0, len(self.player_list)-1)
        return player1_index, player2_index
    
    def start_battle(self):
        '''
        試合開始
        '''
        player1_index, player2_index = self.match_random()
        battle = Battle(self.player_list[player1_index], self.player_list[player2_index])
        battle.start()
        battle.judge_winer()
        self.battle_record.append(battle)

class Player():

    def __init__(self, name: str):
        '''
        プレイヤーを管理
        '''
        self.name = name
        self.win_count = 0
        self.lose_count = 0
        self.draw_count = 0

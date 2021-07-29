from zyanken import Zyanken
from battle import Battle
from player import Player

def main():
    # ジャンケンインスタンスを定義
    zyanken = Zyanken()

    # プレイヤーを登録
    zyanken.register_player(
        Player(name="たんじろう")
        )
    zyanken.register_player(
        Player(name="いのすけ")
        )
    zyanken.register_player(
        Player(name="ぜんいつ")
        )

    # プレイヤー表示
    zyanken.show_all_players()

    # バトルを開始
    for i in range(1, 10):
        zyanken.start_battle()
        zyanken.show_all_players()

    # 履歴を表示
    zyanken.show_battle_record()


main()
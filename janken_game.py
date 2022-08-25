# coding UTF-8
import random

class Janken:

    # 数字と手を対応させる辞書
    hand_dict = {1: 'グー', 2: 'チョキ', 3: 'パー'}

    # 勝敗カウント
    def __init__(self):

        self.win = 0
        self.lose = 0

    # プレイヤーの手を決めるやつ
    def get_player_hand(self):

        self.player_hand = int(input("出す手を選んでください(グー:1, チョキ:2, パー:3)："))

        if self.player_hand not in  [1, 2, 3]:
            print("もう一度入力してください")
            self.get_player_hand()

    # 相手の手を決めるやつ
    def get_opponent_hand(self):

        self.opponent_hand = random.randint(1, 3)
    
    # 勝敗を決めるやつ
    def judge(self):

        match = self.opponent_hand - self.player_hand
        self.result = ''

        if match % 3 == 1:
            self.result = '勝ち'
            self.win += 1
        elif match % 3 == 2:
            self.result = '負け'
            self.lose += 1
        else:
            self.result = 'あいこ'
    
    # 結果を出力するやつ
    def print_judge(self):

        print(f'あなたの手：{self.hand_dict[self.player_hand]}')
        print(f'あいての手：{self.hand_dict[self.opponent_hand]}')

        if self.result != 'あいこ':
            if self.win == 3 or self.lose == 3:
                print(f'{self.win}勝 {self.lose}敗')
            else:
                print(f'現在 {self.win}勝 {self.lose}敗')

    # ゲームの進行するやつ
    def match(self):

        self.get_player_hand()
        self.get_opponent_hand()
        self.judge()
        self.print_judge()


# 以下本文

print("ジャンケンをしよう。いいか、３本先取だ。（cv. 岸辺露伴）")

game = Janken()

while True:

    # ３勝でループから抜ける
    if game.win == 3:
        print("あなたの勝ち！")
        break

    # ３敗でループから抜ける
    if game.lose == 3:
        print("あなたの負け...")
        break

    # 本体を実行
    game.match()

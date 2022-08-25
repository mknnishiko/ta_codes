# coding UTF-8
import random

class Game():

    # ゲームをクリアしたかどうか
    state = 'miss'

    # 初期化処理
    def __init__(self):

        print("数当てゲームを始めます。３桁の数を当ててください！")

        # 初期化するときに答えも決める
        self.decide_answer()
    
    # 答えを決めるやつ
    def decide_answer(self):

        # ３桁の答えをリストで持つ
        self.ans_array = []

        for i in range(3):
            num = random.randint(0, 9)
            self.ans_array.append(num)
    
    # 予想を決めるやつ
    def decide_prediction(self):

        # プレイヤーが予想した数字もリストで持つ
        self.pre_array = []

        for i in range(1, 4):
            num = int(input(f'{i}桁目の予想を入力（０〜９）>> '))
            self.pre_array.append(num)
    
    # 答えと予想を比べるやつ
    def compare_array(self):

        self.hit = 0
        self.ball = 0

        for i, ans_num in enumerate(self.ans_array):
            for j, pre_num in enumerate(self.pre_array):
                # 答えのリストと予想のリストを比べる
                if ans_num == pre_num:
                    # 同じ位置の数字が一緒だったら hit が１増える
                    if i == j:
                        self.hit += 1
                    # 違う位置の数字が一緒だったら ball が１増える
                    else:
                        self.ball += 1
        
        # ３ヒットでクリア
        if self.hit == 3:
            self.state = 'clear'
        else:
            self.state = 'miss'
    
    # 結果を出力するやつ
    def print_result(self):

        # クリアした時の出力
        if self.state == 'clear':
            print(f'{self.hit}ヒット！ 正解です！')
        # クリアしなかった時の出力
        else:
            print(f'{self.hit}ヒット {self.ball}ボール！')
            # ゲームを続けるかどうか
            flag = input('続けますか？ 1：つづける　2：やめる >> ')
            if flag == '2' or flag == '２':
                self.state = 'clear'


# 以下本文
game = Game()

while True:
    # 予想を入力
    game.decide_prediction()
    # 答えと予想を比べる
    game.compare_array()
    # 結果を出力する
    game.print_result()

    # ゲームをクリアしたらループから抜けて終了する
    if game.state == 'clear':
        break

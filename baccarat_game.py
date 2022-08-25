# coding UTF-8
import random

class Game:

    # 初期化処理
    def __init__(self):

        self.card_stack = ['♤1', '♤2', '♤3', '♤4', '♤5', '♤6', '♤7', '♤8', '♤9', '♤10', '♤11', '♤12', '♤13',
                        '♡1', '♡2', '♡3', '♡4', '♡5', '♡6', '♡7', '♡8', '♡9', '♡10', '♡11', '♡12', '♡13',
                        '♧1', '♧2', '♧3', '♧4', '♧5', '♧6', '♧7', '♧8', '♧9', '♧10', '♧11', '♧12', '♧13',
                        '♢1', '♢2', '♢3', '♢4', '♢5', '♢6', '♢7', '♢8', '♢9', '♢10', '♢11', '♢12', '♢13']
        
        self.winner = ''
        self.forecast = ''
        self.natural_win = False
    
    # どちらが勝つか予想する処理
    def forecast_winner(self):

        print("どちらが勝つか予想してください")
        forecast = input("（1：プレイヤー　2：バンカー　3：タイ）>> ")
        if forecast == '1' or forecast == '１':
            self.forecast = 'player'
        elif forecast == '2' or forecast == '２':
            self.forecast = 'banker'
        elif forecast == '3' or forecast == '３':
            self.forecast = 'draw'
        else:
            input("もう一度入力してください")
            self.forecast_winner()
    
    # どちらが勝ったか判定する処理
    def judge(self, player_num, banker_num):

        if player_num == banker_num:
            self.winner = 'draw'
        elif player_num > banker_num:
            self.winner = 'player'
        elif banker_num > player_num:
            self.winner = 'banker'
    
    # 結果を表示する処理
    def show_result(self):

        if game.winner == 'draw':
            input("引き分け")
        else:
            if game.natural_win:
                input("ナチュラルウィン！")
            
            if game.winner == 'player':
                winner = 'プレイヤー'
            else:
                winner = 'バンカー'

            input(f'{winner}の勝ち！')
        
        if game.forecast == game.winner:
            input("予想成功！")
        else:
            input("予想失敗...")

    # 互いにカードを引く処理
    def draw_cards(self):

        if len(player.hand_array) == 2:
            player.check_draw_third()

        if player.can_draw:
            input(f'プレイヤーが{len(player.hand_array) + 1}枚目のカードを引きます')
            player.draw_card()
        
        if len(banker.hand_array) == 2:
            banker.check_draw_third()
        
        if banker.can_draw:
            input(f'バンカーが{len(banker.hand_array) + 1}枚目のカードを引きます')
            banker.draw_card()

    # 互いの手札を表示する処理
    def show_hand(self):

        print()
        print("＝＝"*10)

        print("プレイヤーの手札：", end='')
        for hand in player.hand_array:
            print(hand, end='')
        print(f' 合計{player.hand_num}')
        
        print("バンカーの手札：", end='')
        for hand in banker.hand_array:
            print(hand, end='')
        print(f' 合計{banker.hand_num}')

        input("＝＝"*10)
        print()

    # ゲームを続けるか選ぶ処理
    def continue_game(self):

        is_continue = input("ゲームを続けますか？（1：続ける 2：やめる）>> ")

        if is_continue == '2' or is_continue == '２':
            return True
        else:
            return False


class Player:

    # 初期化処理
    def __init__(self):

        self.hand_array = []
        self.hand_total = 0
        self.hand_num = 0
        self.can_draw = True

    # カードを引く処理
    def draw_card(self):
        
        card = random.choice(game.card_stack)
        self.hand_array.append(card)
        if int(card[1:]) >= 10:
            self.hand_total += 10
        else:
            self.hand_total += int(card[1:])
        self.hand_num = int(str(self.hand_total)[-1])
        game.card_stack.remove(card)

        if self == player:
            input(f'引いたカード：{card}')
        else:
            input(f'引いたカード：{card}')
    
    def check_draw_third(self):

        if self.hand_num <= 5:
            self.can_draw = True
        else:
            self.can_draw = False


class Banker(Player):
    
    # 3枚目のカードを引くか決める処理（バンカー版）
    def check_draw_third(self):
        
        is_draw = False

        if len(player.hand_array) == 2:
            if self.hand_num <= 5:
                is_draw = True
        else:
            if self.hand_num <= 2:
                is_draw = True
            elif self.hand_num == 3:
                if int(player.hand_array[2][1]) <= 7:
                    is_draw = True
            elif self.hand_num == 4:
                if 2 <= int(player.hand_array[2][1]) <= 7:
                    is_draw = True
            elif self.hand_num == 5:
                if 4 <= int(player.hand_array[2][1]) <= 7:
                    is_draw = True
            elif self.hand_num == 6:
                if 6 <= int(player.hand_array[2][1]) <= 7:
                    is_draw = True
        
        self.can_draw = is_draw


# 以下本文
input("「バカラをしよう」")

while True:

    # 実体化
    game = Game()
    player = Player()
    banker = Banker()

    # 予想の入力
    game.forecast_winner()

    # カードを２枚引く
    for i in range(2):
        game.draw_cards()

    # お互いの手札を表示
    game.show_hand()

    # ナチュラルウィンの時
    if player.hand_num >= 8 or banker.hand_num >= 8:
        # 判定
        game.judge(player.hand_num, banker.hand_num)

        # 引き分け以外の場合（ナチュラルウィンの時は出力を追加する為）
        if game.winner != 'draw':
            game.natural_win = True

    # ナチュラルウィン以外の時
    else:
        # 追加でカードを引く
        game.draw_cards()

        # 追加で引いた時は改めて手札を表示
        if len(player.hand_array) == 3 or len(banker.hand_array) == 3:
            game.show_hand()

        # 判定
        game.judge(player.hand_num, banker.hand_num)

    # 結果の表示
    game.show_result()
    
    # 続けるか否か
    if game.continue_game():
        break

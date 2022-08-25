# coding UTF-8
import random


class Game:

    # 合計値の上限（定数）
    Limit = 21

    # 初期化処理
    def __init__(self):

        # 山札のリスト
        self.card_stack = ['♤1', '♤2', '♤3', '♤4', '♤5', '♤6', '♤7', '♤8', '♤9', '♤10', '♤11', '♤12', '♤13',
                           '♡1', '♡2', '♡3', '♡4', '♡5', '♡6', '♡7', '♡8', '♡9', '♡10', '♡11', '♡12', '♡13',
                           '♧1', '♧2', '♧3', '♧4', '♧5', '♧6', '♧7', '♧8', '♧9', '♧10', '♧11', '♧12', '♧13',
                           '♢1', '♢2', '♢3', '♢4', '♢5', '♢6', '♢7', '♢8', '♢9', '♢10', '♢11', '♢12', '♢13']

        # 結果コメントの辞書
        self.result_sentence = {'player': "あなたの勝ちです！",
                                'dealer': "あなたの負けです...",
                                'draw': "引き分けです",
                                'burst': "どちらもバーストしてしまった為、ディーラーの勝ちです"}

        # 勝者（試合結果）
        self.winner = ''

    # 最初にカードを配る処理
    def deal_cards(self):

        input("２枚ずつカードが配られます")

        for i in range(2):
            player.draw_card()
            dealer.draw_card()

        dealer.show_hand_first()
        player.show_hand()

    # 勝敗を決める処理
    def judge(self):

        if player.hand_total > self.Limit and dealer.hand_total > self.Limit:
            self.winner = 'burst'

        elif player.hand_total > self.Limit:
            self.winner = 'dealer'

        elif dealer.hand_total > self.Limit:
            self.winner = 'player'

        elif player.hand_total == dealer.hand_total:
            self.winner = 'draw'

        elif player.hand_total > dealer.hand_total:
            self.winner = 'player'

        elif dealer.hand_total > player.hand_total:
            self.winner = 'dealer'

    # 結果を表示する処理
    def show_result(self):

        print("〜〜" * 7)
        print(f'あなたの手札の合計：{player.hand_total}')
        print(f'ディーラーの手札の合計：{dealer.hand_total}')
        input("〜〜" * 7)

        print(self.result_sentence[self.winner])


class Player:

    # 初期化処理
    def __init__(self):

        self.hand_array = []
        self.hand_total = 0
        self.is_draw = True

    # カードを引く処理
    def draw_card(self):

        card = random.choice(game.card_stack)
        self.hand_array.append(card)

        if int(card[1:]) >= 10:
            self.hand_total += 10
        else:
            self.hand_total += int(card[1:])

        game.card_stack.remove(card)

    # 手札を表示する処理
    def show_hand(self):

        hand = ''
        for card in self.hand_array:
            hand += card

        if self == player:
            person = 'あなた'
        else:
            person = 'ディーラー'

        print(f'{person}の手札：{hand}　合計：{self.hand_total}')

    # 引いたカードを表示する処理
    def show_card(self):

        input(f'引いたカード：{self.hand_array[-1]}')

    # ヒットするか選ぶ処理
    def choice_to_hit(self):

        if player.hand_total > game.Limit:
            player.is_draw = False
            input(f'現在の手札の合計は{self.hand_total}です。{game.Limit}を超えてしまいました...')
            return False

        print(f'現在の手札の合計は{self.hand_total}です。どうしますか？')
        reply = input("（1：ヒット　2：ステイ）>>> ")

        if reply in ['1', '１']:
            self.is_draw = True
        elif reply in ['2', '２']:
            self.is_draw = False
        else:
            print("もう一度入力してください")
            self.choice_to_hit()


class Dealer(Player):

    # ディーラーの合計値が足りなかった時にカードを引く処理
    def more_draw_card(self):

        while dealer.hand_total <= 16:

            input("ディーラーの手札が17に満たないのでもう一枚カードを引きます。")
            dealer.draw_card()
            dealer.show_card()

    # 最初に一枚だけ手札を公開する処理
    def show_hand_first(self):

        input(f'ディーラーの１枚目：{dealer.hand_array[0]}')

    # 手札を公開する処理（ディーラー版）
    def show_hand(self):

        input("ディーラーの手札を公開します。")

        for i, card in enumerate(dealer.hand_array):
            input(f'{i + 1}枚目：{card}')

        print(f'ディーラーの手札の合計は{self.hand_total}です。')

    # カードを表示する処理（ディーラー版）
    def show_card(self):

        input(f'引いたカード：{self.hand_array[-1]}　合計：{self.hand_total}')


# 以下本文
input("ブラックジャックをしよう")

game = Game()
player = Player()
dealer = Dealer()

game.deal_cards()

while True:

    player.choice_to_hit()

    if player.is_draw:
        player.draw_card()
        player.show_card()
    else:
        break

dealer.show_hand()
dealer.more_draw_card()

game.judge()
game.show_result()

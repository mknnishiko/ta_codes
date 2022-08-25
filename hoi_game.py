# coding UTF-8
from janken_game import Janken
import random

class Hoi:

    def __init__(self):

        self.direct_dict = {1:'右', 2:'左', 3:'上', 4:'下'}
        self.result = 'retry'
        self.finger_direct = ''
        self.face_direct = ''
    

    def player_offence(self):

        self.finger_direct = int(input("どこを指差しますか？（1：右　2：左　3：上　4：下）"))
    

    def opponent_offence(self):

        self.finger_direct = random.randint(1, 4)
    

    def player_defence(self):

        self.face_direct = int(input("どこを向きますか？（1：右　2：左　3：上　4：下）"))
    

    def opponent_defence(self):

        self.face_direct = random.randint(1, 4)
    

    def judge(self):
        


    def is_offence(self):

        print("あっち向いて...")

        self.player_offence()
        self.opponent_defence()

        input("ホイ！")
        print(f'あなたが指した向き：{self.direct_dict[self.finger_direct]}')
        input(f'相手が向いた向き：{self.direct_dict[self.face_direct]}')

#coding UTF-8
import itertools

# ↓標準入力から持ってくるやつ
r = 3
array = [[2, 2, 1],
        [1, 3],
        [3, 4, 6, 5]]

# arrayの先頭の数字いらないので消す     new_array = [[2, 1], [3], [4, 6, 5]]
new_array = [line[1:] for line in array]

# itertoolsモジュールのproduct関数 の引数に new_array の中のリストを渡す    num_array = itertools.product([2, 1], [3], [4, 6, 5])
#                                                                    num_array = [(2, 3, 4), (2, 3, 6), (2, 3, 5), (1, 3, 4), (1, 3, 6), (1, 3, 5)]
# リスト名の頭に * をつけることで、リストの中身を展開しつつ引数を渡すことができる
num_array = itertools.product(*new_array)

nums = []

# num_array の中にはタプル型で３つの数字が入っているので、３つの数字を３桁の数値に直す
# nums = [234, 236, 235, 134, 136, 135]
for item in list(num_array):
    num = ""
    for i in item:
        num += str(i)
    nums.append(int(num))

# nums の中身全部足す
result = sum(nums)
# 指定の数で割る
ans = result % (10**9 + 7)
# 出力
print(ans)

# four-square4.py 四平方定理(Lagrange's four-square theorem)
# coding: utf-8
# 大分類 四平方定理
# 中分類 数学
# 小分類 四平方定理の解を求める
# 参考 転用元のfour-square.pyを連続範囲で動かせるように改造
#
# 特色 mathライブラリを使用。sqrt()

from math import *

# 判定用。４個の変数で与えられた整数で平方の解を求める
def verification(n1,n2,n3,n4):
  result_i = n1**2 + n2**2 + n3**2 + n4**2
  return result_i

# 値の平方根を求め、さらに整数部分を返す
def square_n(n):
  result_s = int(sqrt(n))
  return result_s

def logic1(n):
  n1 = 0
  n2 = 0
  n3 = 0
  n4 = 0
  if n == 0:
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
  else:
    n1 = square_n(n) # 1個目の整数
    if n == verification(n1,n2,n3,n4):
      n2 = 0
      n3 = 0
      n4 = 0
    else:
      n2 = square_n(n - n1**2) # 2個目の整数
      if n == verification(n1,n2,n3,n4):
        n3 = 0
        n4 = 0
      else:
        n3 = square_n(n - n1**2 - n2**2) # 3個目の整数
        if n == verification(n1,n2,n3,n4):
          n4 = 0
        else:
          n4 = square_n(n - n1**2 - n2**2- n3**2) # 4個目の整数
  return n1,n2,n3,n4

def logic2(n,n1):
  n1 = n1 - 1 # 1個目の整数から１引く
  n2 = 0
  n3 = 0
  n4 = 0
  if n == verification(n1,n2,n3,n4):
    n2 = 0
    n3 = 0
    n4 = 0
  else:
    n2 = square_n(n - n1**2) # 2個目の整数
    if n == verification(n1,n2,n3,n4):
      n3 = 0
      n4 = 0
    else:
      n3 = square_n(n - n1**2 - n2**2) # 3個目の整数
      if n == verification(n1,n2,n3,n4):
        n4 = 0
      else:
        n4 = square_n(n - n1**2 - n2**2- n3**2) # 4個目の整数
  return n1,n2,n3,n4


# Main1 整数を入力し、四平方定理の解を出力する
inputLine = input("Please Enter NumberOfTimes: ")
NumberOfTimes = int(inputLine)

print('Logic1 Start')
answerTable1=[]
NG_Table1=[]
NG_List1=[]
for n in range(NumberOfTimes):
  n1,n2,n3,n4 = logic1(n)
  # 求めた値と検算結果をリスト化してanswerTable1に格納
  if n == verification(n1,n2,n3,n4):
    result = 'OK  '
  else:
    result = 'NG! '
    NG_List1 = [result,n,n1,n2,n3,n4]  # 結果がNGになった整数をNG_List1に格納
    NG_Table1.append(NG_List1)
  answerList1=[result,n,n1,n2,n3,n4] # 結果をanswerList1に格納
  answerTable1.append(answerList1)        # answerList1をさらにanswerTable1に格納

# Main2 判定結果がNGとなった回答を違うロジックで再計算する
print('Logic2 Start')
answerTable2=[]
for j in range(len(NG_Table1)):
  n  = NG_Table1[j][1]
  n1 = NG_Table1[j][2]
  n1,n2,n3,n4 = logic2(n,n1)
  # 求めた値と検算結果をリスト化してanswerTable2に格納
  if n == verification(n1,n2,n3,n4):
    result = 'OK  '
  else:
    result = 'NG! '
  answerList2=[result,n,n1,n2,n3,n4]
  answerTable2.append(answerList2)

# Main3 判定結果がNGとなった回答を違うロジックで再計算する
NG_counter2 = 0
for i in range(NumberOfTimes):
  if answerTable2[i][0]=='NG! ':
    print(answerTable2[i])
    NG_counter2 = NG_counter2 + 1 
print('NG_counter2=',NG_counter2)


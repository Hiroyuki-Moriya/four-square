# four-square.py 四平方定理(Lagrange's four-square theorem)
# coding: utf-8
# 大分類 四平方定理
# 中分類 数学
# 小分類 四平方定理の解を求める
# 参考
#
# 特色 mathライブラリを使用。sqrt()

from math import *
# 検算用。リストで与えられた４個の整数で平方の解を求める
def verification(m):
  result_v = 0
  for i in range(4):
      result_v = int(m[i])**2 + result_v
  return result_v

# 判定用。４個の変数で与えられた整数で平方の解を求める
def IndividualVariable(n1,n2,n3,n4):
  result_i = n1**2 + n2**2 + n3**2 + n4**2
  return result_i

# 値の平方根を求め、さらに整数部分を返す
def square_n(n):
  result_s = int(sqrt(n))
  return result_s

# Main 整数を入力し、四平方定理の解を出力する
m = []
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n = int(input())
if n != 0:
  n1 = square_n(n) # 1個目の整数
  if n == IndividualVariable(n1,n2,n3,n4):
    n2 = 0
    n3 = 0
    n4 = 0
  else:
    n2 = square_n(n - n1**2) # 2個目の整数
    if n == IndividualVariable(n1,n2,n3,n4):
      n3 = 0
      n4 = 0
    else:
      n3 = square_n(n - n1**2 - n2**2) # 3個目の整数
      if n == IndividualVariable(n1,n2,n3,n4):
        n4 = 0
      else:
        n4 = square_n(n - n1**2 - n2**2- n3**2) # 4個目の整数

m.append(n1)
m.append(n2)
m.append(n3)
m.append(n4)

# 求めた値のリストと検算結果の出力
if n == verification(m):
  result = 'OK'
else:
  result = 'NG'
print('n=',n,m,result)
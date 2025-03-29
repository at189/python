# n = int(input("請輸入數字:"))
# n = int(n)
# if n % 2 == 0:
#     print("數字是偶數")
# else:
#     print("數字是奇數")

# 匯入模組
# import turtle
# import turtle as t

# from turtle import *
# from turtle import  done#匯入模組turtle的當中的done指令

# done()
# turtle.done()

# t.speed(0)  # 設定速度
# t.forward(100)  # 前進100步
# t.right(90)  # 右邊向前轉90度
# t.forward(100)  # 前進100步
# t.right(90)  # 右邊向前轉90度
# t.forward(100)  # 前進100步
# t.right(90)  # 右邊向前轉90度
# t.forward(100)  # 前進100步
# t.done()  # 讓視窗不要關閉

# for example
# for的組成有三個部分
# for回圈變數 in 範圍:
# 迴圈變數只能活在for回圈中
# 迴圈變數每回合都會從範圍中取出一個值
for i in range(10):  # range(10)的範圍是0到9
    print(i)
for i in range(1, 6):  # range=1到5
    print(i)

for i in range(1, 6, 2):  # range=1,3,5
    print(i)

import turtle as t

t.speed(0)  # 設定速度
for i in range(4):
    t.forward(150)  # 前進100步
    t.right(90)  # 右邊向前轉90度
    t.done()  # 讓視窗不要關閉

import turtle

turtle.color("red")  # 設定顏色
turtle.shape("turtle")  # 設定形狀
turtle.stamp()  # 蓋章
turtle.penup()  # 提筆

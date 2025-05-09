"""
作業說明:
讓turtle蓋出一個時鐘數字的位置
總共會蓋出12個印章
"""

# t.home()#讓烏龜回到原點的指令的指令
# import turtle as t

# t.color("yellow")
# t.pensize(5)
# t.penup()
# t.shape("turtle")
# t.fillcolor("yellow")
# t.begin_fill()
# for i in range(5):
#     t.forward(200)
#     t.right(144)
# t.end_fill()
# t.done()

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j)
"""
使用turtle 繪製時鐘
"""

"""
輸入一數字n為尋找的區間範圍, 找出區間範圍
3,7的倍數顯示在螢幕上, 其餘不顯示
hint:可以使用%取餘數進行判斷
EX
請輸入正整數:20
3
6
7
9
12
14
15
18
"""

"""
請輸入要印出的箭頭大小
hint:
可利用字串乘法
>>>val="*" * 3
>>>print(val)
>>>***
EX:
請輸入要印出的箭頭大小:3
  *
 ***
*****
  *
  *
  *
"""

# import turtle as t
# import time

# t.color("orange")
# t.speed(0)

# for i in range(60):
#     t.right(6 * i)
#     t.forward(80)
#     time.sleep(1)
#     t.home()
#     t.clear()


# n = int(input("請輸入整數: "))


# for i in range(1, n + 1):
#     if i % 3 == 0 or i % 7 == 0:
#         print(i)


# import turtle as t


# t.penup()
# for i in range(13):
#     t.forward(100)
#     t.stamp()
#     t.home()
#     t.right(30 * i)
# t.done()

n = int(input("請輸入要印出的箭頭大小:"))

for i in range(1, n + 1):
    print(f" " * (n - i) + "*" * (2 * i - 1))
for i in range(1, n + 1):
    print(f" " * (n - 1) + "*")

"""
測量你的BMI值, 確認你的體重是否正常?
* BMI公式:體重(公斤) / 身高(公尺)的平方
* BMI值正常範圍:14.8到20.7之間
* BMI值過重範圍:20.7以上
EX:
請輸入身高(公尺):1.7
請輸入體重(公斤):45
你的BMI為15.570934256055365
體重過輕
請輸入身高(公尺):1.7
請輸入體重(公斤):60
你的BMI為20.761245674740486
體重正常
請輸入身高(公尺):1.7
請輸入體重(公斤):90
你的BMI為31.14186851211073
體重過重
"""

# try:
#     h = float(input("請輸入身高(公尺):"))
#     w = float(input("請輸入體重(公斤):"))
#     bmi = w / h**2
#     if bmi < 14.8:
#         print("體重過輕")

#     elif bmi > 20.7:
#         print("體重過重")
#     else:
#         print("體重正常")
# except:
#     print("請輸入數字")
# # 參考code
# import turtle as t

# t.penup()
# t.color("red")
# t.shape("turtle")
# for i in range(120):
#     t.forward(20)
#     t.stamp()
#     t.right(10)

# t.done()
# for i in range(4):


# t.penup()
# t.color("red")
# t.shape("turtle")
import turtle as t

t.penup()
t.shape("turtle")
for i in range(50):
    t.forward(8 * i)
    t.right(55)
    t.stamp()
    # 設定形狀
t.done()  # 讓視窗不要關閉

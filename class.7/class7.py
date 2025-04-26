f = int(input("請使用者輸入一個數字"))
a = "是質數"
for i in range(2, f):
    if f % i == 0:
        a = "不是質數"

print(f"{f} {a}")
# 輸入的數字除以迴圈變數，接著拿餘數判斷是否是0

# for...else
# 當for迴圈正常結束時,執行else區塊的程式
# exaample
for i in range(5):
    print(i)
else:
    print("for迴圈正常結束")

# while...else
# 當while迴圈正常結束時,執行else區塊的程式
# exaample:
i = 0
while i < 5:
    print(i)
    i = i + 1
else:
    print("while迴圈正常結束")


import time

s = int(input("請使用者輸入倒數計時秒數"))


for i in range(s, -1, -1):
    print(i)
    time.sleep(1)
else:
    print("時間到!")

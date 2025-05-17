juices_list = ["蘋果汁", "柳橙汁", "葡萄汁", "系統關閉"]


while True:
    print("請選一個果汁")
    print("1. 蘋果汁")
    print("2. 柳橙汁")
    print("3. 葡萄汁")
    print("4. 系統關閉")

    number = input("請輸入編號：")

    if number == "1":
        print("你點的是 蘋果汁 ")
    elif number == "2":
        print("你點的是 柳橙汁 ")
    elif number == "3":
        print("你點的是 葡萄汁 ")
    elif number == "4":
        print("系統關閉")
        break
    else:
        print("輸入錯勿")


import random

r = random.randrange(1, 100)
import random

print(random.randint(1, 100))
print(random.randrange(1, 101))
ans = random.randint(1, 100)
while True:
    x = int(input("請輸入1到100的整數: "))
    if x == ans:
        print("正確")
        break
    elif x < ans:
        print("太小了")
    elif x > ans:
        print("太大了")

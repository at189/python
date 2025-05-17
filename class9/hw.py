juices_list = ["蘋果汁", "柳橙汁", "葡萄汁", "系統關閉"]


while True:
    for i in range(len(juices_list)):
        print(f"{i + 1}.{juices_list[i]}")
    try:
        n = int(input("請輸入編號："))
    except:
        print("查無此編號")
        continue
    if n == len(juices_list):
        print("系統關閉")
        break
    elif 1 <= n < len(juices_list):
        print(f"{juices_list[n-1]}")
    else:
        print("查無此編號")


import random

big = 100
small = 0
r = random.randrange(1, 100)  # 1到100的隨機數
while True:
    x = int(input(f"請輸入一個{small}到{big}的整數: "))
    if x == r:
        print("正確")
        break
    elif x < r:
        print("太小了")
        if x > small:
            small = x
    elif x > r:
        print("太大了")
        if x < big:
            big = x

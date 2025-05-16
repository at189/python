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

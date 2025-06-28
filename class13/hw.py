fruits = {"蘋果": 25, "香蕉": 20, "橘子": 30}
print("水果價格查詢系統")
while True:
    print("目前水果價格:")
    for fruit, price in fruits.items():
    print("1.新增水果價格")
    print("2.修改水果價格")
    print("3.刪除水果")
    print("4.離開系統")

    choice=input("請輸入1到4：")
    print("="*26)
    if choice=="1":
        fruit_name=input("請輸入水果名稱：")
        if fruit_name in fruits:
            print("水果已存在")
            
        else:
            price=int(input(f"請輸入{fruit_name}水果價格："))
            fruits[fruit_name]=price
            print(f"{fruit_name}水果價格已修改為{price}元")

    elif choice=="2":
        fruit_name=input("請輸入要改的水果名稱：")
        if fruit_name in fruits:
            new_price=int(input(f"請輸入{fruit_name}水果價格："))
            fruits[fruit_name]=new_price
            print(f"{fruit_name}水果價格修改為{new_price}元")
            
        else:
            print("水果不存在")
    elif choice=="3":
        fruit_name=input("請輸入要刪除的水果名稱：")
        if fruit_name in fruits:
            fruits.pop(fruit_name)
            print(f"{fruit_name}水果已刪除")
        else:
            print("水果不存在")
    elif choice=="4":
        print("再見")
        break



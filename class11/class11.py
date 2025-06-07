# 複製List,避免原本的List被更動
L = ["hello", "world"]
L2 = L.copy()  # 使用copy()複製List
print(L2)  # ["hello", "world"]
L2[0] = "python"  # 修改複製後List的索影0資料
print(L)  # ["python", "world"]原本的List不影響
print(L2)  # ["python", "world"]複製後的List可以影響
# 這跟變數的=賦値不同,一般情況下會開2個記憶體空間
# 在List的情況下使用=會讓兩個變數名稱指向同一個記憶體空間
# 這導致修改一個List會影響到另一個List
# 所以在需要複製List時,應該使用copy()方法

# remove()刪除指定位置的資料
L = ["hello", "world", "python"]
L.remove("world")  # 移除"world"
print(L)  # ["hello", "python"]

# pop()刪除最後一個資料
L = ["hello", "world", "python"]
# 不給索引時,pop()會刪除最後一個資料
L.pop()  # 刪除最後一個資料
print(L)  # ["hello", "world"]
s = L.pop(1)  # 刪除索引1的資料
print(s)  # world
print(L)  # ['hello']


# """
# 你是一位「購物小幫手」！幫媽媽記下要買的東西，還能修改、刪除，或是看看清單裡有什麼。
# 📋 你可以做這些事：
# 程式會在每一步自動顯示目前的購物清單。
# 1️⃣ 新增東西
#     ➕ 加到清單最後（append）
#     📌 新增到清單中的某個位置（insert）
# 2️⃣ 修改東西
#     ✏️ 輸入編號，換掉舊項目
# 3️⃣ 刪除東西
#     ❌ 用名稱刪除（remove）
#     🗑️ 用位置刪除（pop）
# 4️⃣ 離開程式
#     👋 不想逛了就回家！

L = []


while True:
    print(L)
    print("1. 加東西")
    print("2. 改東西")
    print("3. 刪東西")
    print("4. 離開")

    選項 = input("請輸入1到4：")

    if 選項 == "1":
        item = input("請輸入東西：")
        print("a. 加到尾端 b. 插入指定位置")
        選項 = input("請輸入a或b：")
        if 選項 == "a":
            L.append(item)
        elif 選項 == "b":
            num = int(input("請輸入插入位置："))
            L.insert(num, item)

    elif 選項 == "2":
        num = int(input("請輸入編號："))
        item = input("請輸入東西：")
        L[num] = item

    elif 選項 == "3":
        print("a. 依名稱刪除 b. 依位置刪除")
        選項 = input("請輸入a或b：")
        if 選項 == "a":
            L.remove(item)
        elif 選項 == "b":
            num = int(input("請輸入刪除位置："))
            L.pop(num)
    elif 選項 == "4":
        print("再見")
        break

    else:
        print("請輸入 1 到 4 ")

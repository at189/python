# append 在程式執行的過程當中可以將列表的最後面
L = ["hello", "world"]
L.append("python")  # 加上python
print(L)

# insert 在程式執行的過程當中可以將列表的最後面
L = ["hello", "world"]
L.insert(1, "python")  # 在索引1加上python
print(L)  # 得到["hello","python","world"]

# 修改特定位置的資料
L = ["hello", "world"]
L[1] = "python"
print(L)

wather = ["晴天", "多雲", "雨天", "多雲", "晴天"]
print(wather)

while True:
    try:
        ans = int(input("請輸入要修改的星期數字(1-7):"))
    except:
        print("請輸入數字編號")
    else:
        if ans > len(wather) or ans < 1:
            print("請輸入正確的編號")
        else:
            print("您要修改得星期是" + str(ans))
            print("原本的天氣是" + wather[ans - 1])
            new_weather = input("請輸入新的天氣:")
            wather[ans - 1] = new_weather
            print("修改後的天氣是" + wather[ans - 1])
            print(wather)
            break


# 🔹 第一行：
# python
# 複製
# 編輯
# wather = ["晴天", "多雲", "雨天", "多雲", "晴天"]
# print(wather)
# 建立一個清單 wather（裡面有 5 天的天氣）

# 印出目前的天氣狀況

# 🔹 接下來是一直重複問你問題的迴圈：
# python
# 複製
# 編輯
# while True:
# 一直重複執行，直到你輸入正確

# 🔹 試著讓你輸入一個數字：
# python
# 複製
# 編輯
#     try:
#         ans=int(input("請輸入要修改的星期數字(1-7):"))
# 問你：「你想改星期幾的天氣？」

# 輸入後，把它變成整數（int）

# 🔹 如果你輸入錯（像是輸入文字）：
# python
# 複製
# 編輯
#     except:
#         print("請輸入數字編號")
# 告訴你：「請輸入數字編號」

# 🔹 如果你輸入正確，接著會檢查：
# python
# 複製
# 編輯
#     else:
#         if ans > len(wather) or ans < 1:
#             print("請輸入正確的編號")
# 檢查你輸入的數字有沒有在 1 到 5 之間（因為只有 5 天）

# 如果不對，就叫你重來

# 🔹 如果沒問題，開始修改天氣：
# python
# 複製
# 編輯
#         else:
#             print("您要修改的星期是" + str(ans))
#             print("原本的天氣是" + wather[ans - 1])
#             new_weather = input("請輸入新的天氣:")
#             wather[ans - 1] = new_weather
#             print("修改後的天氣是" + wather[ans - 1])
#             print(wather)
#             break
# 顯示你選的是星期幾

# 顯示那天原本的天氣

# 讓你輸入新的天氣

# 把舊的天氣換掉

# 顯示修改後的結果

# 用 break 跳出迴圈，程式結束

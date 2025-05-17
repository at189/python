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
        ans=in
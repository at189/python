# 字典(Dictionary);用來儲存[key-value]配對的資料結構
# 字典很適合用來表示有對應關係的資料,像是商品和價格的對應

# 建立字典:使用大括號{},key和value之間用冒號:分隔
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(d)

# 從字典中取得特定key對應的value
# 如果key不存在keyerror錯誤
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(d["蘋果"])
# print(d["梨子"])#這會產生keyerror錯誤

# 遍歷字典:有多種方式可以走訪字典中的資料
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}

# 1.從字典中取出所有的key
for k in d:
    print(k)  # 印出key名稱
    print(d[k])  # 用key來取得對應的value

# 2.明確使用keys()方法來取得所有的key
for k in d.keys():
    print(k)  # 印出key名稱
    print(d[k])  # 用key來取得對應的value

# 3.使用values()方法來取得所有的value
for v in d.values():
    print(v)  # 直接印出value,但不知道對應的key

# 4.使用items()方法同時來取得key和value
# 這是最常用的方法,因為它可以同時儲存key和value
for k, v in d.items():
    print(f"{k}:{v}")  # 印出key和value

# 新增字典/修改字典的內容
# 直接指定key對應的value,如果key已存在則修改,否則加入
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
d["蘋果"] = 10  # 修改字典中的蘋果的value為10
print(d)
d["蓮霧"] = 15  # 加入字典中的蓮霧
print(d)

# 刪除字典中的內容
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
d.pop("蘋果")  # 刪除字典中的蘋果
# 如果要刪除的key不存在,則會產生keyerror,可以加上第二個參數,當key不存在時,不會有任何變化
popitem = d.pop("蓮霧", "不存在這筆資料")  # 不會有任何變化
print(d)  # {"香蕉":30,"橘子":25}
print(popitem)


# len:取得字典中有多少組key-value配對
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(len(d))


# 檢查某個key是否存在
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
# 使用前先檢查可以避免keyerror錯誤
print("蘋果" in d)  # True,因為字典中有蘋果
print("蓮霧" in d)  # False,因為字典中沒有蓮霧


# 檢查某個元素中有沒有在list中
# 使用in可以快速檢查某個元素是否在於list中
L = [1, 2, 3, 4, 5]
print(3 in L)  # True,3在list中

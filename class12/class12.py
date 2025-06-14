# index:尋找指定元素在List中第一次出現的位子
# 如果元素不存在會產生錯誤,所以使用前建議先檢查元素是否存在
L = [1, 2, 3, 4, 5]
print(L.index(3))  # 找到數字3在1的位子

# count:尋找指定元素在List中總共出現的位子
# 這個方法很適合用來檢查重複資料的計算
L = ["hello", "world", "python", "hello"]
print(L.count("hello"))  # 找到數字hello共出現2次

# sort:將List排序
# 這個方法可以將List排序後再存入List中
L = [1, 2, 3, 4, 5]
L.sort()
print(L)

# sort(reverse=True):將List排序中由大到小
# sort(reverse=True)參數可以讓排序相反
L = [1, 2, 3, 4, 5]
L.sort(reverse=True)
print(L)

# reverse:將List倒序
# 這不是排序,只是把第一個變成最後一個,把最後一個變成第一個
L = [1, 2, 3, 4, 5]
L.reverse()
print(L)

# List和字串有很多相似的操作方式
# 我們我們可以像操作字串一樣來處理

# 合併兩個List:使用+運算子兩個List合併
# 這會產生一個全新的List,不會改變原本的List
L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = L1 + L2  # 把L1和L2合併成一個全新的List
print(L3)

# 重複List中的內容:使用*運算子讓List重複多次
# 這在建立重複資料時很有用
L = [1, 2, 3]
L = L * 3  # 重複L三次
print(L)

# 不同資料型態之間的轉換技巧
print(range(10))  # range本身看不到內容,只是產生一個範圍描述
print(list(range(10)))  # 可以將range轉換成可以看到具體內容list
print(list("Hello"))  # 可以將字串轉換成list

# split:將一個完整的字串按照指定的分隔符號切割成多個部分
# 這是處理文件資料的好方法
s = "hello world"
L = s.split("")  # 將s切割成多個部分
print(L)
calendar = "2020/12/25"
L = calendar.split("/")  # 以斜線作為分點來切割日期字串
print(L)

# join:將List或字串合併成一個完整的字串
# 可以指定要用什麼符號來連接這些字串
L = ["hello", "world"]
s = " ".join(L)  # 將L連接成成一個字串
print(s)

birthday = "2023/10/20"
birthday = birthday.split("/")
birthday = "-".join(birthday)
print(birthday)

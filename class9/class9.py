import random  # 隨機模組

# random.randrange設定範圍的方式跟range一樣﹐特性也一樣不包含最後一個數字
# random.randrange的功能是隨機取得一個數字,range是產生一組數字
print(random.randrange(10))  # 從0到9隨機取得一個數字
print(random.randrange(1, 10))  # 從1到9隨機取得一個數字
print(random.randrange(1, 10, 2))  # 從{1,3,5,7,9}中隨機取得一個數字
# random.randint設定範圍一調要有開始跟束
# 不能跳數字抽遷


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

# list 清單
# list 可以存入很多種類的資料,每筆資料用','分隔
# list 可以存入不型態的資料
# list 最外層用'[]'包起來
L = [1, 2, 3, 4, 5]  # 數字
print(L)
# 不同型態混合
L = [1, 2, 3, 4, 5, "hello", ["world", 6]]  # 數字,字串,list
print(L)

# List 取值
# list 取值方式跟字串一樣,用'[]'取值
# list 取值方式跟字串一樣,也可以用'[:]'取值

# 設定範圍的方式跟Range很像,不包含結尾
print(L[1:4:2])  # 取出第2到4的值,間隔為2
print(L[0:3])  # 取出第1到3的值
print(L[:3])  # 取出第4到最後的值
print(L[:])  # 取出所有值

# list len 列表長度
L = [1, 2, 3, 4, 5]
print(len(L))  # 取得List的長度,也就是List當中有幾筆資料

# 務必不要跟index混淆,index是資料的編號,len是資料的數量

# len可以搭配for迴圈使用
for i in range(len(L)):
    print(L[i])

for i in L:
    print(i)

# 要使要使用哪一種方式讀取List,要看使用的情境當中會不會要用到index

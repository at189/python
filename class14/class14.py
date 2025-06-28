# def
# 新增一個函數要用def開頭,後面接著函數名稱,再加上小括號,最後加上冒號
# 小括號裡面可以放入傳入函數的參數也可以不放
def hello():
    print("hello,world")


for i in range(10):
    hello()


# 有傳入參數的函數
# 這個函數有一個參數,叫做name,當呼叫這個函數時,可以傳入一筆資料給name
def hello(name):
    print(f"hello,{name}!")


hello("Alice")
hello("Bob")
hello("Charlie")
for i in range(10):
    hello("i")  # 這裡的i會被當作name的值

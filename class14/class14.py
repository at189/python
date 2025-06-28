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


# 有回傳值的函數
# 這個函數會回傳一個值,當呼叫這個函數時,可以把迴傳的值存起來
# 在指令當中只要執行return,就會回傳值,並結束函數
def add(a, b):  # 可以允許多個傳入參數
    return a + b


print(add(1, 2))
print(add("hello", "world"))
sum = add(3, 4)
print(sum)


# 有多個回傳值的函數
# 這個函數會回傳兩個值,當呼叫這個函數時,可以把迴傳的值存起來
def add_sub(a, b):
    return a + b, a - b


sum, sub = add_sub(5, 6)  # 可以將回傳值存到多個變數中
print(f"sum={sum},sub={sub}")


# 多個 return
def add_sub(a, b):
    if a > b:
        return a + b
    else:
        return a - b


print(add_sub(5, 6))
print(add_sub(6, 5))


# 預設參數
# 可以在函數的參數中設定預設值,當呼叫這個函數時,如果沒有傳入值,就會使用預設值
# 多個參數時,有預設值的參數要放在沒有預設值的參數後面
def hello(name, message="hello"):
    print(f"{message},{name}!")


# 如果是def hello(message="hello",name)會出錯因為有預設值的參數要放在沒有預設值的參數後面
hello("Alice")
hello("Bob", "good morning")


# def區域變數與全域變數
length = 5  # 全域變數


def colculate_square_area():
    area = length**2  # length是全域變數,area是區域變數

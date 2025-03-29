# try except
# 錯誤處理
try:
    # 嘗試執行可能出現的錯誤的程式碼
    n = int(input("input a number:"))

except:
    # 如果執行程式碼時發生錯誤，則執行下列程式碼
    print("you should input a number")

else:
    # 如果執行程式碼沒有錯誤，則執行下列程式碼
    print(n + 1)


try:
    h = float(input("請輸入身高:"))
    w = float(input("請輸入體重:"))
    bmi = w / h**2
    print(f"你的bmi為{bmi}")
except:
    print("請輸入有效的數字")

# 比較運算子
print(1 == 1)  # true,因為1等於1
print(1 != 1)  # false,因為1不等於1
print(1 < 1)  # false,因為1不小於1
print(1 > 1)  # false,因為1不大於1
print(1 <= 1)  # true,因為1小於等於1
print(1 >= 1)  # true,因為1大於等於1

# 邏輯運算子
# and 代表全部條件都滿足才會回傳true
# or 代表全部條件都滿足才會回傳false
# not 代表反轉數值

print(True and True)  # true true和ture
print(True and False)  # false, false和false
print(False and False)  # false,false和false
print(True or True)  # true ,truec或true
print(True or False)  # true, true或true
print(False or False)  # false, false或false
print(not True)  # false，not true
print(not False)  # true ，not false

password = input("請輸入密碼:")
if password == "5678910":
    print("密碼正確")
    print("歡迎光臨")
else:
    print("密碼錯誤")

# if elif else
pwd = input("請輸入密碼:")
if pwd == "123456":
    print("歡迎光臨")
elif pwd == "5678910":
    print("歡迎光臨")
else:
    print("密碼錯誤")

# if elif elseg是連續的判斷，只要有一個條件成立，後面的判斷就不會執行
# if一定要有，elif可以有多個，else可以沒有

try:
    grade = int(input("請輸入成績:"))
    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")
    elif grade >= 60:
        print("D")
    else:
        print("F")
except:
    print("請輸入數字")

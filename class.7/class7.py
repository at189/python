f = int(input("請使用者輸入一個數字"))
a = "是質數"
for i in range(2, f):
    if f % i == 0:
        a = "不是質數"

print(f"{f} {a}")

"""
輸入一組整數範圍，將範圍中的所有質數顯示於畫面上。
EX:
請輸入開始整數:10
請輸入結束整數:50
11
13
17
19
23
29
31
37
41
43
47
"""

f = int(input("請輸入開始整數"))
a = int(input("請輸入結束整數"))
for n in range(f, a + 1):
    if n > 1:
        ans = "是質數"
        for i in range(2, n):
            if n % i == 0:
                ans = "不是質數"

        if ans == "是質數":
            print(n)

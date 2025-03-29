"""
請使用者輸入華氏溫度
如果使用者輸入的不是數字，則會顯示"輸入錯誤!"
如果輸入數字則會將華氏轉換為攝氏溫度並顯示出來(轉換公式可以上網搜尋喔!)

操作範例如下:

請輸入華氏溫度:60
華氏溫度60.0F等於攝氏溫度15.555555555555555C

請輸入華氏溫度:ABC
輸入錯誤!

"""


def fahrenheit_to_celsius():
    try:
        f = float(input("請輸入華氏溫度: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"華氏溫度{fahrenheit}F等於攝氏溫度{celsius}C")
    except:
        print("輸入錯誤!")


def grade_judgment(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "E"


score = int(input("請輸入成績："))
print(f"您的等第為：{grade_judgment(score)}")

try:
    f = float(input("請輸入華氏溫度:"))
    c = (fahrenheit - 32) * 5 / 9
    print(f"華氏溫度{fahrenheit}F等於攝氏溫度{celsius}C")
except:
    print("輸入錯誤!")

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
        fahrenheit = float(input("請輸入華氏溫度: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"華氏溫度{fahrenheit}F等於攝氏溫度{celsius}C")
    except ValueError:
        print("輸入錯誤!")


fahrenheit_to_celsius()

"""
請將下列變數做出正確的型態分類
apple = 1000
age = 12
minor = False
name = "David"
weight = 64.5
zip = "545"
int(整數)  :apple.age
bool(布林) :minor
str(字串)  :name.zip
float(浮點數、小數):weight
"""

"""
請問Python有哪四種形態:<字串><整數><浮點數><布林>

請問使用什麼指令可以顯示出形態
答案:type

請問今天學了哪一些指令(函式)?
答案:
input、print、int、float、str、bool、type、max、len
延續上題, 請嘗試描述每個指令的功能各別是什麼?
答案:
input:讓使用在終端在終端機輸入資料
print:的誇弧內可以放入"提示字串
int:將輸入的資料轉換成整數
float:將輸入的資料轉換成浮點數
str:將輸入的資料轉換成字串
bool:將輸入的資料轉換成布林值
type:取得參數的型態
max:最大值
len:字串長度
"""
"""
請使用者輸入身高(公尺)h以及體重(公斤)w
透過下面公式計算出BMI數值並顯示計算結果
bmi = w/h**2
EX:
請輸入身高:1.7
請輸入體重:50
你的BMI為17.30103806228395
"""
h = float(input("請輸入身高:"))
w = float(input("請輸入體重:"))
bmi = w / h**2
print("你的BMI為", bmi)

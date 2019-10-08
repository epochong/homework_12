dict = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine"
}
tel = input("请输入电话号码：")
for i in range(0,len(tel)):
    print(dict.get(int(tel[i])),end=" ")
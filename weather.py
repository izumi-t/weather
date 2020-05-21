import sys
import tkinter as tk
import tkinter.messagebox as tkm
import requests
from bs4 import BeautifulSoup

root = tk.Tk()
root.title("今日の天気")
root.geometry("400x500")


# ボタンが押されたら呼び出される関数
def GetEntry(event):
    # Entry1の値を取得
    Entry1_value = Entry1.get()
    print(Entry1_value)


def showMessage(text):
    tkm.showinfo("info", text)

# checkboxのチェック状況を取得する
def check(event):
    global val1
    global val2
    global val3

    text = ""

    if Val1.get() == True:
        text += "天気:{}".format(weather)+"\n"
    else:
        text += ""

    if Val2.get() == True:
        text += "最高気温:{} {}".format(temp_max,temp_max_diff)+"\n"
    else:
        text += ""

    if Val3.get() == True:
        text += "最高気温:{} {}".format(temp_min,temp_min_diff)+"\n"
    else:
        text += ""

    if text =="":
        tkm.showinfo("項目が選択されていません")
    else:
        tkm.showinfo("info",Entry1.get()+"の今日の天気予報は\n"+ text +"です")



#tenki.jpの目的の地域のページのURL(京都市)
url = "https://tenki.jp/forecast/6/29/6110/26100/"

#HTTPリクエスト
r = requests.get(url)

bsObj = BeautifulSoup(r.content, "html.parser")

# 今日の天気情報はclass="today-weather"の中にある
today = bsObj.find(class_="today-weather")

# pタグの中に天気
weather = today.p.string

# divタグ（class="date-value-wrap"）の中にある
temp = today.div.find(class_="date-value-wrap")

#ddタグをすべて取り出す
temp = temp.find_all("dd")

#最高気温
temp_max = temp[0].span.string

#最高気温の前日比
temp_max_diff = temp[1].string

#最低気温
temp_min = temp[2].span.string

#最低気温の前日比
temp_min_diff = temp[3].string


# チェックボックスの各項目の初期値
Val1 = tk.BooleanVar()
Val2 = tk.BooleanVar()
Val3 = tk.BooleanVar()

Val1.set(True)
Val2.set(True)
Val3.set(True)

# Entryを出現
Entry1 = tk.Entry(width=30)
Entry1.insert(tk.END, "京都市")
Entry1.pack()

# checkboxを出現
CheckBox1 = tk.Checkbutton(text="天気", variable=Val1)
CheckBox1.pack()
CheckBox2 = tk.Checkbutton(text="最高気温", variable=Val2)
CheckBox2.pack()
CheckBox3 = tk.Checkbutton(text="最低気温", variable=Val3)
CheckBox3.pack()

# buttonを出現
button1 = tk.Button(root, text=u'天気を検索',width=30)
button1.bind("<Button-1>",check)
button1.pack()






root.mainloop()

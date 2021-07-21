import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
from turtle import  *

win1 = tk.Tk()
win1.title('MY main')  # 添加窗体名称
win1.geometry('670x470')  # 设置窗体大小


def msgbox():
        color('red', 'yellow')

        begin_fill()
        while True:
            forward(200)
            left(170)
            if abs(pos()) < 1:
                break
        end_fill()
        done()
def he():
    os.system("C:\Windows\System32/mspaint.exe")

Button(win1, text="自动画太阳", command=msgbox).pack()
Button(win1, text="自己画", command=he).pack()

win1.mainloop()

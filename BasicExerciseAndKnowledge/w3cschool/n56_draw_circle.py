#coding:utf-8
# 题目：画图，学用circle画圆形

from Tkinter import *

canvas = Canvas(width=800, height=600, bg='yellow')  
canvas.pack(expand=YES, fill=BOTH)                
k = 1
j = 1
for i in range(1,26):
    canvas.create_oval(310 - k,250 - k,310 + k,250 + k, width=1)
    k += j
    j += 0.3

mainloop()

#这个东西并不重要 重要的是了解Tkinter这个module
#GUI界面,tkinter
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

#打开文档
def load():
    with open(filename.get()) as file:
        contents.delete('1.0', tk.END)
        contents.insert('end',file.read())

#保存文档
def save():
    with open(filename.get(), 'w') as file:
        file.write(contents.get('1.0', tk.END))

#清空内容
def clear():
    contents.delete('1.0', tk.END)

top = tk.Tk()            #创建主窗口
top.title('Editor')      #设置窗口标题
top.iconbitmap('Title.ico')     #设置窗口图标

contents = ScrolledText(font=('Arial',12),bg='#F5F5F5',fg='#000000')  #ScrolledText可滚动的多行文本区域
#设置文本区域side对齐底部，expand可随窗口拖动变化大小，fill填充区域
contents.pack(side='bottom',expand=True,fill='both')
filename = tk.Entry(font=('Arial',10),bg='#D3D3D3',fg='#0000CD')    #创建单行文本框，并设置字体，背景色,前景色
filename.pack(side='left',expand=True,fill='x')   #设置文本框属性

tk.Button(activebackground='#00BFFF',text='Open',command=load).pack(side='left')     #打开按键
tk.Button(activebackground='#00BFFF',text='Save',command=save).pack(side='left')     #保存按键
tk.Button(activebackground='#00BFFF',text='Clear',command=clear).pack(side='left')   #清空按键

#按钮点击时的动作
# def btn_clinked():
#     print('Button clicked')
#
# def clink_callback(event):
#     print(event.x, event.y)

# btn = tk.Button()        #创建一个按钮
# btn.pack()               #放置按钮，默认放在父控件中
# btn.config(text='Clinked me', command=btn_clinked)       #设置按钮属性
# tk.Label(text="i'm the first windows").pack()            #创建一个标签
# top.bind('<Button-1>', clink_callback)

#second = tk.Toplevel()   #创建另一个窗口
#tk.Label(second, text="i'm the second windows").pack()

# for i in range(10):              #创建一系列按钮
#     tk.Button(text=i,width=5,height=1).pack()

top.mainloop()           #主循环，进主循环才会显示界面






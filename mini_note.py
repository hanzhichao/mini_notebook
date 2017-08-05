# coding:utf-8
from Tkinter import *
from tkMessageBox import *
from tkFileDialog import *
import tkFileDialog
import os

# resolve UnicodeEncodeError
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

file_name = ''

# 作者
def author():
    showinfo('作者信息', '本软件由韩志超完成')

# 版权信息
def about():
    showinfo('版权信息', '本软件版权由韩志超所有')


# 新建
def new():
    global file_name
    root.title('未命名文件')
    file_name = None
    text_box.delete(1.0, END)


# 打开
def open_file():
    global file_name
    file_name = askopenfilename(defaultextension='.txt')
    if file_name == '':
        file_name = None
    else:
        root.title('FileName: '+ os.path.basename(file_name))
        text_box.delete(1.0, END)
        with open(file_name, 'r') as f:
            text_box.insert(1.0, f.read())


# 另存为
def save_as():
    global file_name
    file_name = asksaveasfilename(initialfile='未命名.txt', defaultextension='.txt')
    with open(file_name, 'w') as f:
        f.write(text_box.get(1.0, END))
    root.title('FileName: ' + os.path.basename(file_name))


# 保存
def save():
    global file_name
    try:
        with open(file_name, 'w') as f:
            msg = text_box.get(1.0, END)
            print msg
            f.write(text_box.get(1.0, END))
        root.title('FileName: ' + os.path.basename(file_name))
    except Exception,e:
        print e.message
        save_as()


# 剪切
def cut():
    text_box.event_generate('<<Cut>>')


# 复制
def copy():
    text_box.event_generate('<<Copy>>')


# 粘贴
def paste():
    text_box.event_generate('<<Paste>>')


# 撤销
def undo():
    text_box.event_generate('<<Undo>>')


# 重做
def redo():
    text_box.event_generate('<<Redo>>')


# 全选
def select_all():
    text_box.tag_add(1.0, END)


# 搜索
def search():


    def gen_search():
        text_box.tag_add(1.0, END)
        print entry1.get()

    top_search = Toplevel(root)
    top_search.geometry('240x30+200+200')
    label1 = Label(top_search, text='Find')
    label1.grid(row=0, column=0, padx=5)
    entry1 = Entry(top_search, width=20)
    entry1.grid(row=0, column=1, padx=5)
    button1 = Button(top_search, text='查找', command=gen_search)
    button1.grid(row=0, column=2)





# ui
root = Tk()
root.title('Mini Note')
root.geometry('600x400+100+100')

# menu_bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# file_menu
file_menu = Menu(menu_bar)
file_menu.add_command(label='新建', accelerator='Ctrl + N', command=new)
file_menu.add_command(label='打开', accelerator='Ctrl + O', command=open_file)
file_menu.add_command(label='保存', accelerator='Ctrl + ', command=save)
file_menu.add_command(label='另存为', accelerator='Ctrl + Shirt + S', command=save_as)
menu_bar.add_cascade(label='文件', menu=file_menu)

# edit_menu
edit_menu = Menu(menu_bar)
edit_menu.add_command(label='撤销', accelerator='Ctrl + Z', command=undo)
edit_menu.add_command(label='重做', accelerator='Ctrl + Y', command=redo)
edit_menu.add_separator()
edit_menu.add_command(label='剪切', accelerator='Ctrl + X', command=cut)
edit_menu.add_command(label='复制', accelerator='Ctrl + C', command=copy)
edit_menu.add_command(label='粘贴', accelerator='Ctrl + V', command=paste)
edit_menu.add_separator()
edit_menu.add_command(label='查找', accelerator='Ctrl + F', command=search)
edit_menu.add_command(label='全选', accelerator='Ctrl + A', command=select_all)
menu_bar.add_cascade(label='编辑', menu=edit_menu)

# help_menu
help_menu = Menu(menu_bar)
help_menu.add_command(label='作者', command=author)
help_menu.add_command(label='版权', command=about)
menu_bar.add_cascade(label='关于', menu=help_menu)

# tool_bar
tool_bar = Frame(root, bg='#eee')
new_button = Button(tool_bar, text='打开', width=5, command=open_file)
open_button = Button(tool_bar, text='保存', width=5, command=save)
new_button.pack(side=LEFT, padx=1, pady=1)
open_button.pack(side=LEFT, padx=1, pady=1)
tool_bar.pack(side=TOP, fill=X)

# status_bar
status_bar = Frame(root, bg='#eee')
status_line = Label(status_bar, text='Ln20', bg='#eee')
status_line.pack(side=LEFT)
status_bar.pack(side=BOTTOM, fill=X)

# line_num_bar
line_num_bar = Label(root, width=2, bg='#eee')
line_num_bar.pack(side=LEFT, fill=Y)

# scroll_bar
scroll_bar = Scrollbar(root)
scroll_bar.pack(side=RIGHT, fill=Y)

# text_box
text_box = Text(root, undo=True)
text_box.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=text_box.yview)
text_box.pack(expand=YES, fill=BOTH)

root.mainloop()
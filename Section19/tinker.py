'''
20-1 Tkinter

tkinter
    Python 에서 기본적으로 제공하는 GUI(Graphical User Interface)프로그램 모듈

    그 외 GUI pyQt
'''

import tkinter as tk
from tkinter import ttk

root= tk.Tk()
label = tk.Label(root,text='Hello,Tkinter!')
label.pack()

entry= tk.Entry(root)
entry.pack()

text = tk.Text(root)
text.pack()
#아래 글을 입력할 수 있는 형태이다

checkbox_var= tk.IntVar()
checkbutton = tk.Checkbutton(root,text='Check Me!', variable= checkbox_var)
checkbutton.pack()

var = tk.StringVar()
var.set('option1')
radiobutton1 = tk.Radiobutton(root, text='Option1', variable=var, value='option1')
radiobutton2 = tk.Radiobutton(root, text='Option2', variable=var, value='option2')
radiobutton1.pack()
radiobutton2.pack()

scale = tk.Scale(root, from_ =0, to=10, orient=tk.HORIZONTAL)
scale.pack()

spinbox= tk.Spinbox(root, from_= 0, to=10)
spinbox.pack()

combo = ttk.Combobox(root, values=['Item 1', 'Item 2', 'Item 3'])
combo.pack()

def onClick():
    print('Button Click')
    s_entry = entry.get()
    s_text = text.get('1.0', tk.END)
    s_radiobutton = var.get()
    i_checkbox_var= checkbox_var.get()
    i_scale = scale.get()
    i_spinbox = spinbox.get()
    s_combo = combo.get()

    print(f's_entry: {s_entry}')
    print(f's_text: {s_text}')
    print(f's_radiobutton: {s_radiobutton}')
    print(f'i_checkbox_var: {i_checkbox_var}')
    print(f'i_scale {i_scale}')
    print(f'i_spinbox: {i_spinbox}')
    print(f's_combo: {s_combo}')

button= tk.Button(root, text= 'Click me!', command=onClick)
button.pack()

root.mainloop()


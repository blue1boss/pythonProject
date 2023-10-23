'''
파일명: Ex20-2-Tkinter.py

Tkinter Layout
    GUI 화면 배치 관련 메서드
'''


import tkinter as tk

root= tk.Tk()
# pack() 메서드는 위젯들을 상자안에 쌓듯이 배치한다.
label1 = tk.Label(root,text="Hello,World")
label1.pack()
label2 =tk.Label(root, text="This is a Sample Program")
label2.pack()

root.mainloop()



#Grid()메서드는 위젯을 격자모양으로 배치한다.
#Row 와 Column으로 위치를 지정한다
root = tk.TK()
label1 = tk.Label(root,text="Hello,World")
label1.grid(row=0 , column=1)
label2 =tk.Label(root, text="This is a Sample Program")
label2.grid(row=1 , column=1)
root.mainloop()

#Place ()메서드는 위젯을 지정된 자표에 배치한다. x,y좌표를 지정
root = tk.Tk()
label1 = tk.Label(root, text="Hello World")
label1.place(x=10,y=10)
label2 = tk.Label(root, text="This is a Sample Program")
label2.place(x=10,y=50)
root.mainloop()
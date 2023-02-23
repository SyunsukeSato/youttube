import tkinter
from tkinter import font

from isort import file

#windowの作成
root = tkinter.Tk()

root.title("label practis")
root.iconbitmap("icon.ico")
root.geometry("550x500")
root.resizable(0 , 0)
root.config(bg = "red")

#ラベルの作成
label1 = tkinter.Label(root , text = "よろしくお願いします")
label1.pack()

label2 = tkinter.Label(root , text = "よろしくお願いします" , font = ("Arial" , 10 , "bold"))
label2.pack()

label3 = tkinter.Label(root , text = "よろしくお願いします" , font = ("Arial" , 10 , "bold") , bg = "gray" , fg="green")
label3.pack(padx=10 , pady=10)

label4 = tkinter.Label(root)
label4.config(text = "よろしくお願いします")
label4.config(bg = "gray")
label4.pack(padx=10 , pady=10 , ipadx=50 , ipady=50 , anchor="w")

label5 = tkinter.Label(root , text = "よろしくお願いします" , font = ("Arial" , 10 , "bold") , bg = "gray" , fg="green")
label5.pack(padx=10 , pady=10 , fill="x")





root.mainloop()




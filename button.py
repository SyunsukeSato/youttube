import tkinter

root = tkinter.Tk()
root.title("button practice")
root.iconbitmap("icon.ico")
root.config(bg="red")
root.geometry("550x500")
root.resizable(0 , 0)

#ボタンの作成
button_1 = tkinter.Button(root , text = "ボタン１")
button_1.grid(row = 0 , column=0)

button_2 = tkinter.Button(root , text = "ボタン2")
button_2.grid(row = 0 , column=1)

button_3 = tkinter.Button(root , text = "ボタン3" , bg = "pink" , activebackground = "red")
button_3.grid(row = 0 , column=2 , padx = 10 , pady= 10 ,ipadx= 10 , ipady= 10 ) 

#columspanは3つのボタンを1つのcolumとして見るという物
button_4 = tkinter.Button(root , text = "ボタン4" , borderwidth=5)
button_4.grid(row = 1 , column=0 , columnspan=3 , sticky="WE") 

button_5 = tkinter.Button(root , text = "ボタン5_test")
button_6 = tkinter.Button(root , text = "ボタン6_test")
button_7 = tkinter.Button(root , text = "ボタン7_test")
button_8 = tkinter.Button(root , text = "ボタン8_test")
button_9 = tkinter.Button(root , text = "ボタン9_test")
button_10 = tkinter.Button(root , text = "ボタン１0_test")


button_5.grid(row = 2 , column=0 , padx=5 , pady=5)
button_6.grid(row = 2 , column=1 , padx=5 , pady=5)
button_7.grid(row = 2 , column=2 , padx=5 , pady=5 , sticky="W")
button_8.grid(row = 3 , column=0 , padx=5 , pady=5)
button_9.grid(row = 3 , column=1 , padx=5 , pady=5)
button_10.grid(row = 3 , column=2 , padx=5 , pady=5 , sticky="W")

root.mainloop()



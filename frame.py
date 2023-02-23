import tkinter

from isort import file

root = tkinter.Tk()
root.title("Frame practice")
root.geometry("550x500")
root.iconbitmap("icon.ico")
root.resizable(0,0)

#なぜフレームを使う？ ⇒　同じwindow上でpackとglidを配置させることができないから
#フレームの作成
frame_1 = tkinter.Frame(root , bg="yellow")
frame_2 = tkinter.Frame(root , bg="green")
frame_3 = tkinter.LabelFrame(root , text = "ラベルフレームです" , borderwidth=5)

frame_1.pack(file = "both" , expand=True)
frame_2.pack(file = "x" , expand=True)
frame_3.pack(file = "both" , expand=True)

root.mainloop()




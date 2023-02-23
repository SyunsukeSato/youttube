import tkinter

#ウィンドウの作成
root = tkinter.Tk()
root.title("windoe practice")
root.iconbitmap("icon.ico")
root.geometry("300x800")

#ウィンドウのサイズ変更禁止
root.resizable(1 , 1)

#背景色を変更する
root.config(bg="red")

#サブウィンドウの作成 装飾の方法はメインウィンドウと同じ
sub_window = tkinter.Toplevel()
sub_window.title("sub window")
sub_window.config(bg = "#123123")
sub_window.geometry("200x300")



#ウィンドウのループ処理
root.mainloop()








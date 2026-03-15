# 主程序
try:
    import tkinter as tk
    import threading
    def open_file():
        with open("E:\\电脑侠\\电脑侠.py",mode="r",encoding="UTF-8")as file:
            return file.read()
    import os
    win = tk.Tk()
    win.geometry("1600x600+-7+30")
    win.title("电脑侠补丁管理器")
    frame1=tk.Frame(win,width=600,height=350)
    scrollbar_x = tk.Scrollbar(frame1, orient="horizontal")
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
    scrollbar = tk.Scrollbar(frame1)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    frame1.place(x=0,y=50)
    text = tk.Text(frame1, yscrollcommand=scrollbar.set, xscrollcommand=scrollbar_x.set, wrap=tk.NONE, font=(None,15),width=150)

    text.pack()


    def move_file(source_path, destination_path):
        # 确保目标路径存在
        # 重命名文件
        try:
            os.remove(destination_path)
            os.rename(source_path, destination_path)
        except:
            pass


    # 使用示例

    def pyexe():
        from tkinter import filedialog,messagebox
        f = "E:\\电脑侠\\电脑侠.py"
        import os
        os.chdir(os.path.dirname(f))
        filename_with_ext = os.path.basename(f)

        # 获取不含格式的文件名
        filename_without_ext = os.path.splitext(filename_with_ext)[0]
        os.system("pyinstaller -F -w " + filename_without_ext + ".py")
        source_file = 'E:\\电脑侠\\dist\\电脑侠.exe'
        destination_file = 'E:\\电脑侠\\电脑侠.exe'

        move_file(source_file, destination_file)
        messagebox.showinfo("成功发送！")
    def decode_text(text):
        lst=[]
        s=""
        for i in text:
            if i!="\n":
                s+=i
            else:
                lst.append(s)
                s=""
        lst1=[""]
        lst2=[]
        cc=0
        ss=""
        for i in lst:
            try:
                if i[0]=="|"and i[1]=="|":
                  cc=1
                  lst2.append(ss)
                  ss=""
                else:
                    if cc!=1:
                        ss+=i
                        ss+="\n"
                    else:
                        lst1.append(i)
                        cc=0
            except:
                if cc != 1:
                    ss += i
                    ss += "\n"
                else:
                    cc = 0
        lst2.append(ss)
        return lst1,lst2
    def pyexe1():
        threading.Thread(target=pyexe).start()
    def save():
        global text
        with open("E:\\电脑侠\\电脑侠.py",mode="w",encoding="UTF-8")as file:
            file.writelines(text.get("1.0",tk.END))
        file.close()
        pyexe1()
    def gi():
        from try_run_code import run123123123123
    def do_it(text1,t):
        bd=text1.get("1.0",tk.END)
        lst1,lst2=decode_text(bd)
        global text
        for i in range(len(lst1)):
            if i!=0:
                text.insert(lst1[i]+".0",lst2[i])
    def try_run(text):
        with open("try_run_code.py",encoding="UTF-8",mode="w")as file:
            file.write(text.get("1.0",tk.END))
        file.close()
        threading.Thread(target=gi).start()


    def new(ttttt):
        root=tk.Tk()
        root.title("快速补丁")
        root.geometry("1600x600+-7+30")
        frame1 = tk.Frame(root, width=600, height=350)
        scrollbar_x = tk.Scrollbar(frame1, orient="horizontal")
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        scrollbar = tk.Scrollbar(frame1)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        frame1.place(x=0, y=50)
        text1 = tk.Text(frame1, yscrollcommand=scrollbar.set, xscrollcommand=scrollbar_x.set, wrap=tk.NONE, font=(None, 15),
                       width=150)

        text1.pack()
        scrollbar_x.config(command=text1.xview)
        scrollbar.config(command=text1.yview)
        global text
        tk.Button(root,text="应用",command=lambda :do_it(text1,text)).place(x=0,y=0)
    scrollbar_x.config(command=text.xview)
    scrollbar.config(command=text.yview)
    text1=open_file()
    tk.Button(win,text="发送补丁",font=(None,20),command=save).place(x=0,y=0)
    tk.Button(win,text="快速补丁",font=(None,20),command=lambda :new(text)).place(x=150,y=0)
    tk.Button(win,text="测试",font=(None,20),command=lambda :try_run(text)).place(x=300,y=0)
    text.insert("1.0",text1)
    win.mainloop()


except Exception as e:
    import sys
    import tkinter as tk
    win=tk.Tk()
    win.attributes("-alpha",0)
    win.overrideredirect(1)
    from tkinter import messagebox
    import traceback

    exc_type, exc_value, exc_traceback = sys.exc_info()

    messagebox.showerror("错误",f"错误类型: {exc_type.__name__}"+"\n"+f"错误信息: {exc_value}"+"\n详细信息:\n"+traceback.format_exc())



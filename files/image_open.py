import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
class image_opener:
    def __init__(self,root):
        self.label=tk.Label(root)
    def place(self,x,y):
        self.label.place(x=x,y=y)
    def put_image(self,file_path):
        if file_path:
            img = Image.open(file_path)

            img_tk = ImageTk.PhotoImage(img)
            self.label.config(image=img_tk)
            self.label.image = img_tk  # 防止垃圾回收


root = tk.Tk()
root.title("图片显示示例")
image=image_opener(root)
image.place(x=0,y=0)
image.put_image("C:\\Users\\Windows\\Desktop\\桌面2\\png\\2.png")
root.mainloop()


import tkinter as tk
from tkinter import filedialog
import os

def select_files():
    files = filedialog.askopenfilenames(filetypes=[("Video Files", "*")])
    for file in files:
        extract_audio(file)

def extract_audio(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
       # f.writelines(lines[12:])
        f.writelines(lines[0:-12])

window = tk.Tk()

# 添加选择文件按钮
from ttkbootstrap import Style
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
window.geometry('150x70')
style = Style()
window = style.master
button = ttk.Button(window, text="选择文件", command=select_files,bootstyle=PRIMARY)
button.pack(anchor="center", padx=0, pady=15)


# 运行主循环
window.mainloop()

import tkinter as tk
from tkinter import filedialog
import os
import re

def batch_regex_replace():
    # 获取用户输入的正则表达式和替换文本
    regex_pattern = regex_entry.get()
    replace_text = replace_entry.get()

    # 创建Tkinter窗口
    root = tk.Tk()
    root.withdraw()

    # 选择文件夹对话框
    folder_path = filedialog.askdirectory(title="选择文件夹")

    # 循环处理文件夹下的所有txt文件
    for filename in os.listdir(folder_path):
        if filename.endswith(".ass"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                content = file.read()

                # 使用正则表达式进行查找和替换
                replaced_content = re.sub(regex_pattern, replace_text, content)

            # 将替换后的内容写回原文件
            with open(file_path, 'w') as file:
                file.write(replaced_content)

    # 处理完成提示
    result_label.config(text="正则替换完成！")

# 创建Tkinter窗口
window = tk.Tk()
window.title("批量正则查找替换")

from ttkbootstrap import Style
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
style = Style()
window.geometry('150x150')
# 创建文本输入框和标签
regex_label = tk.Label(window, text="正则表达式：")
regex_label.pack()
regex_entry = tk.Entry(window)
regex_entry.pack()

replace_label = tk.Label(window, text="替换：")
replace_label.pack()
replace_entry = tk.Entry(window)
replace_entry.pack()

# 创建按钮
button = tk.Button(window, text="开始正则替换", command=batch_regex_replace)
button.pack()

# 创建结果标签
result_label = tk.Label(window, text="")
result_label.pack()

# 运行窗口主循环
window.mainloop()

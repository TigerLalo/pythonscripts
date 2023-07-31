#再改
import os
import tkinter as tk
from tkinter import filedialog


def modify_file_extension(folder_path, current_extension, new_extension):
    for filename in os.listdir(folder_path):
        if filename.endswith(current_extension):
            current_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, filename.replace(current_extension, new_extension))
            os.rename(current_file_path, new_file_path)


def browse_folder():
    folder_path = filedialog.askdirectory(initialdir="/", title="Select Folder")
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)


def modify_files():
    folder_path = folder_entry.get()
    current_extension = current_extension_entry.get()
    new_extension = new_extension_entry.get()

    if folder_path and current_extension and new_extension:
        modify_file_extension(folder_path, current_extension, new_extension)
        result_label.config(text="文件修改成功！")
    else:
        result_label.config(text="请填写完整信息！")


# 创建主窗口
window = tk.Tk()
window.title("批量修改文件后缀")

# 文件夹路径选择
folder_label = tk.Label(window, text="选择文件夹：")
folder_label.pack()
folder_entry = tk.Entry(window)
folder_entry.pack()
browse_button = tk.Button(window, text="浏览", command=browse_folder)
browse_button.pack()

# 当前后缀输入
current_extension_label = tk.Label(window, text="当前后缀：")
current_extension_label.pack()
current_extension_entry = tk.Entry(window)
current_extension_entry.pack()

# 新后缀输入
new_extension_label = tk.Label(window, text="新后缀：")
new_extension_label.pack()
new_extension_entry = tk.Entry(window)
new_extension_entry.pack()

# 修改按钮
modify_button = tk.Button(window, text="修改文件", command=modify_files)
modify_button.pack()

# 结果标签
result_label = tk.Label(window)
result_label.pack()

# 运行主循环
window.mainloop()

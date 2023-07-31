import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
import os
def compress_audio():
    # 选择音频文件夹
    folder_path = filedialog.askdirectory()
    
    # 遍历文件夹中的音频文件
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".mp3") or file_name.endswith(".wav"):
            # 读取音频文件
            audio = AudioSegment.from_file(os.path.join(folder_path, file_name))
            
            # 压缩音频（这里使用了一半的音频质量，可根据需要进行调整）
            compressed_audio = audio.export(os.path.join(folder_path, "compressed_" + file_name), format="mp3", bitrate="128k")
            
            # 输出压缩后的文件路径
            print("压缩后的文件: " + os.path.join(folder_path, "compressed_" + file_name))

# 创建 Tkinter 应用程序窗口
root = tk.Tk()

# 添加按钮
compress_button = tk.Button(root, text="批量压缩音频", command=compress_audio)
compress_button.pack()

# 运行 Tkinter 事件循环
root.mainloop()

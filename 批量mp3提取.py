import tkinter as tk
from tkinter import filedialog
import os
from moviepy.editor import VideoFileClip



def select_files():
    files = filedialog.askopenfilenames(filetypes=[("Video Files", "*.mp4;*.avi;*.mkv")])
    for file in files:
        extract_audio(file)

def extract_audio(video_file):
    filename = os.path.splitext(video_file)[0]
    output_file = f"{filename}_audio.wav"

    video = VideoFileClip(video_file)
    audio = video.audio

    audio.write_audiofile(output_file, codec="pcm_s16le")
    print(f"成功从 {video_file} 中提取音频并保存为 {output_file}")


# 添加选择文件按钮
from ttkbootstrap import Style
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
window = tk.Tk()
window.geometry('150x70')
style = Style()
window = style.master
button = ttk.Button(window, text="选择文件", command=select_files,bootstyle=PRIMARY)
button.pack(anchor="center", padx=0, pady=15)


# 运行主循环
window.mainloop()

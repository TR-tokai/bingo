import tkinter as tk
import random

# ウィンドウ設定
root = tk.Tk()
root.title('Bingo')
root.geometry('500x500')
root.resizable(True, True)
root.state('zoomed')
button_font_size = 20
number_font_size = 200

# 配置
frame = tk.Frame(root)
# スタート、ストップ、リセットボタン
start_button = tk.Button(frame, text='スタート', font=('', button_font_size)).grid(row=4, column=0)
stop_button = tk.Button(frame, text='ストップ', font=('', button_font_size)).grid(row=4, column=1)
reset_button = tk.Button(frame, text='リセット', font=('', button_font_size)).grid(row=4, column=2, padx=10)
# 抽選した番号表示ラベル
number = tk.Label(root, text='BINGO', font=('', number_font_size)).pack(anchor=tk.CENTER, expand=1)
frame.pack(side='left', anchor=tk.S)

root.mainloop()
import time
import random
import re
import tkinter as tk
from tkinter import filedialog

# ルートウィンドウを作成する
root = tk.Tk()
root.withdraw()

# ファイル選択ダイアログを表示する
file_path = filedialog.askopenfilename()

# テキストファイルから文章を取得する
with open(file_path, encoding='utf-8') as f:
    text = f.read()

# 正規表現で2字か4字の漢字の熟語を抽出する
pattern = re.compile("[\u4e00-\u9fff]{2}(?:[\u4e00-\u9fff]{2})?")
words = pattern.findall(text)

# 熟語を隠してから1秒ごとに表示する
for word in words:
    # 熟語を隠す処理
    hidden_word = '*' * len(word)
    text = text.replace(word, hidden_word)

    # 熟語を表示する処理
    print(text)
    print('\r' + word, end='', flush=True)
    time.sleep(1)

print('\n\nすべての熟語を表示しました。')

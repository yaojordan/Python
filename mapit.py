#! python3

import webbrowser
import sys
import pyperclip


#sys.argv 儲存program的檔名
#若參數沒有輸入地址, 則直接取用剪貼簿的地址
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

#@+leo-ver=4-thin
#@+node:amd_yen.20130308221230.2458:@shadow c2/docutils_ex1.py
#coding: utf-8
#@<< docstring >>
#@+node:amd_yen.20130308221230.3823:<< docstring >>
'''
1. 由 http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt 下載 rst 格式檔案
2. 利用本程式轉為 html, 然後以 Chrome 開啟檢查
3. 由 url 取得文件內容
import urllib.request
url = 'http://example.com/'
resp = urllib.request.urlopen(url)
data = resp.read()          # 傳回一個 'bytes' 物件
text = data.decode('utf-8') # 將 'bytes' 物件內容編碼成為 'string'
參考資料: 
http://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3
'''
#@-node:amd_yen.20130308221230.3823:<< docstring >>
#@nl
#@<< import >>
#@+node:amd_yen.20130308221230.3824:<< import >>
# 導入 os 模組
import os
'''
以下經由 urllib 向網路 URL 取得文件內容
'''
# 導入 urllib.request
import urllib.request
# 導入用來處理 rst2html 的 publish_string
from docutils.core import publish_string
#@-node:amd_yen.20130308221230.3824:<< import >>
#@nl
rst檔案網址 = "http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt"
# 開啟網址內容
網址回覆 = urllib.request.urlopen(rst檔案網址)
# 取得 url 所在主機的內容標頭檔案
print(urllib.request.urlopen(rst檔案網址).headers)
# 取得目標網址的 byte 物件
byte資料 = 網址回覆.read()
# 解碼後得到文件內容
文件內容 = byte資料.decode('utf-8')
# 列印出文件內容
#print(文件內容)
# 利用 docutils.core 模組中的 publish_string() 方法, 將 rst 內容轉為 html
超文件內容 = publish_string(
        source=文件內容,
        writer_name='html',
        settings = None,
        settings_overrides={'output_encoding': 'unicode'}
    )
# 將超文件內容存成檔案
檔案 = open("docutils_ex1.html", "w")
檔案.write(超文件內容)
目前所在目錄 = os.getcwd()
os.system("V:/tools/GoogleChromePortable/GoogleChromePortable.exe "+目前所在目錄+"/docutils_ex1.html")
# 關閉檔案
檔案.close()
#@<< comment >>
#@+node:amd_yen.20130308221230.3825:<< comment >>
'''
# rst檔案1 = "http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt"
# 執行 rst2html.py, rst 檔案為輸入, 而 html 檔案作為輸出
# 將已經存在的 1.txt rst 格式檔案利用 rst2html.py 轉為 1.html
os.system("V:/SciTE/python.exe V:/SciTE/scripts/rst2html.py V:/misc/rst_test/1.txt v:/misc/rst_test/1.html")
所產生的超文件 = "v:/misc/rst_test/1.html"
# 以 Chrome 開啟所建立的 html 檔案
os.system("V:/tools/GoogleChromePortable/GoogleChromePortable.exe "+所產生的超文件)
'''
#@-node:amd_yen.20130308221230.3825:<< comment >>
#@nl
#@-node:amd_yen.20130308221230.2458:@shadow c2/docutils_ex1.py
#@-leo

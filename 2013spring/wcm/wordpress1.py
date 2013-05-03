#coding: utf-8
import xmlrpc.client
import datetime
import os
os.environ['TZ'] = 'Asia/Taipei'

網誌網址 = "http://wordpress.2012c1.hostingsiteforfree.com/xmlrpc.php"
網誌帳號 = "account"
網誌密碼 = "password"
wp_blogid = "0"

status_draft = 0
status_published = 1

server = xmlrpc.client.ServerProxy(網誌網址)

網誌標題 = "以現在時間上傳網誌, 再試一次"
網誌內容 = "這是以 Python 程式新增的網誌內容!\n並且進行跳行\n前面這裡跳行.<!--more-->在字串中嵌入內容"
網誌內容 +="<pre lang=\"python\" line=\"1\" colla=\"+\">"
網誌內容 +='''
#coding: utf-8
import xmlrpc.client
import datetime
import os
os.environ['TZ'] = 'Asia/Taipei'

wp_url = "https://WordPress 網誌網址/xmlrpc.php"
wp_username = "帳號"
wp_password = "密碼"
wp_blogid = "0"

status_draft = 0
status_published = 1

server = xmlrpc.client.ServerProxy(wp_url)

title = "以現在時間上傳網誌, 再試一次"
content = "這是以 Python 程式新增的網誌內容!\n並且進行跳行\n前面這裡跳行.<!--more-->"
content +="<pre lang=\"python\" line=\"1\" colla=\"+\">"
content +=\'''
#coding: utf-8
import xmlrpc.client
import datetime
import os
os.environ['TZ'] = 'Asia/Taipei'
for 索引 in range(10):
    print("測試")
\'''
# 請注意, 以下的 /pre 標駐要拿掉兩個反斜線?
content +="\</pre\>"
# 指定時間出版
#date_created = xmlrpc.client.DateTime(datetime.datetime.strptime("2013-01-01 00:00", "%Y-%m-%d %H:%M"))
# 以現在時間出版, 考慮與 Server 時間差八個小時 (480 分鐘), 因此要在 8 個小時前發表
date_created = xmlrpc.client.DateTime(datetime.datetime.strptime((datetime.datetime.now()-datetime.timedelta(minutes=480)).strftime('%Y-%m-%d %H:%M'),"%Y-%m-%d %H:%M"))
categories = ["Uncategorized"]
tags = ["python", "測試"]
data = {'title': title, 'description': content, 'dateCreated': date_created, 'categories': categories, 'mt_keywords': tags}

post_id = server.metaWeblog.newPost(wp_blogid, wp_username, wp_password, data, status_published)

'''
網誌內容 +='''</pre>'''
# 指定時間出版
#date_created = xmlrpc.client.DateTime(datetime.datetime.strptime("2013-01-01 00:00", "%Y-%m-%d %H:%M"))
# 以現在時間出版, 考慮與 Server 時間差八個小時 (480 分鐘), 因此要在 8 個小時前發表
建立時間 = xmlrpc.client.DateTime(datetime.datetime.strptime((datetime.datetime.now()-datetime.timedelta(minutes=480)).strftime('%Y-%m-%d %H:%M'),"%Y-%m-%d %H:%M"))
類別 = ["Uncategorized"]
關鍵字 = ["python", "測試"]
出版資料 = {'title': 網誌標題, 'description': 網誌內容, 'dateCreated': 建立時間, 'categories': 類別, 'mt_keywords': 關鍵字}

post_id = server.metaWeblog.newPost(wp_blogid, 網誌帳號, 網誌密碼, 出版資料, status_published)

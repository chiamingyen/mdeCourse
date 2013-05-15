#coding: utf-8
import cherrypy, os
# 執行指令但是不要開啟 Windows shell 用
import subprocess

class 網際類別(object):
	def index(self, *args, **kwargs):
		r = cherrypy.response
		r.headers['Content-Type'] = 'text/plain'
		content = "Positional arguments\n\n"
		for k in args:
		  content += k + "\n"
		content += "\nKeyword arguments\n\n"
		for k in kwargs:
		  content += k + ": " + kwargs[k] + "\n"
		return content
	index.exposed = True

# 由於 url 帶有 &, 無法直接使用 os.system() 開啟網頁同時派送變數, 因此改用 subprocess
url = 'http://localhost:8088/index/pos1/pos2?var1=2&var2=2&var3=3'
chrome = "V:/tools/GoogleChromePortable/GoogleChromePortable.exe"
retcode = subprocess.call([chrome, url])

cherrypy.server.socket_port = 8088
cherrypy.server.socket_host = '127.0.0.1'
cherrypy.quickstart(網際類別())

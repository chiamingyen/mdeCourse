#coding: utf-8
 
import cherrypy
# 執行指令但是不要開啟 Windows shell 用
import subprocess
 
class MyClass(object):
    def index(self):
        return "執行 MyClass!"
    index.exposed = True
 
class MyChanger(object):
    _cp_config = {
        'tools.sessions.on': True
    }
 
    myclass = MyClass()
 
    def doReturn(self, amount=None):
        if amount != "":
            amount = float(amount)
        else:
            return "輸入有問題!<br /><br /><a href=\"/\">重新換算</a>"
        output = "要找回的總數為: "+str(amount)+" 元<br /><br />"
        總額 = amount
        反算 = 0
        換錢組合 = ()
        for 紙鈔與銅板 in [2000,1000,500,100,25,10,1]:
            換幾張 = int(總額/紙鈔與銅板)
            #print("換幾張為",換幾張)
            output += str(紙鈔與銅板)+"元,需要"+str(換幾張)+"個 <br />"
            # 換錢組合變數的運算
            換錢組合 += (紙鈔與銅板,)*換幾張
            總額 -= 紙鈔與銅板*換幾張
            output += "總額為"+str(總額)+"<br />"
            反算 += 紙鈔與銅板*換幾張
            output += "反算為"+str(反算)+"<br />"
        output += "<br /><a href=\"/\">重新換算</a>"
        return output
 
    doReturn.exposed = True
 
    def index(self):
        return """<html>
<head>
  <title>網路找錢程式</title>
</head>
<body>
  <form action="doReturn" method="post">
    請輸入要找給客戶的總額:<input type="text" name="amount" value="" 
        size="15" maxlength="40"/>
    <p><input type="submit" value="進行換算"/></p>
    <p><input type="reset" value="清除"/></p>
  </form>
</body>
</html>"""		
 
    index.exposed = True
 
 # 由於 url 帶有 &, 無法直接使用 os.system() 開啟網頁同時派送變數, 因此改用 subprocess
url = 'http://localhost:8088/index'
chrome = "V:/apps/GoogleChromePortable/GoogleChromePortable.exe"
retcode = subprocess.call([chrome, url])

# 指定程式執行的連接埠號, 內定為 8080
cherrypy.server.socket_port = 8088
# 指定程式執行所對應的伺服器 IP 位址, 內定為 127.0.0.1
cherrypy.server.socket_host = '127.0.0.1'
cherrypy.quickstart(MyChanger())

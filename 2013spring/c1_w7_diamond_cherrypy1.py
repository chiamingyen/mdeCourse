#coding: utf-8
# c1w7_1.py, 這個程式示範如何將菱形列印程式由單機搬到 OpenShift
import cherrypy
class HelloWorld(object):
    def index(self):
        return "Hello World!"
    index.exposed = True

    @cherrypy.expose
    def diamond(self, num=5):
        # 將 num 字串轉為整數
        n = int(num)
        數列1 = [x+n for x in range(0, n)]
        數列2 = list(range(n, 0, -1))
        數列3 = zip(數列1, 數列2)
        outstring = ""
        for i in 數列3:
            for j in range(2*n):
                if j == i[0] or j == i[1]:
                    #print("*", end="")
                    outstring += "*"
                else:
                    #print(" ", end="")
                    outstring +="&nbsp;"
            #print()
            outstring +="<br />"

        數列4 = [x for x in range(2, n+1)]
        數列5 = [x+n-2 for x in range(n, 0, -1)]
        數列6 = zip(數列4, 數列5)
        for i in 數列6:
            for j in range(2*n):
                if j == i[0] or j == i[1]:
                    #print("*", end="")
                    outstring += "*"
                else:
                    #print(" ", end="")
                    outstring +="&nbsp;"
            #print()
            outstring +="<br />"

        return outstring

# 單機使用
cherrypy.quickstart(HelloWorld())
# OpenShift 平台上使用
#application = cherrypy.Application(HelloWorld())

#@+leo-ver=5-thin
#@+node:amd_yen.20130429221223.10917: * @file GMail.py
#encoding: utf-8
# 這是整個程式的主要功能物件


#@@language python
#@@tabwidth -4

#@+<<declarations>>
#@+node:amd_yen.20130429221223.10918: ** <<declarations>> (GMail)
import smtplib,threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#@-<<declarations>>
#@+others
#@+node:amd_yen.20130429221223.10919: ** class GMail
class GMail(object): 
    #@+others
    #@+node:amd_yen.20130429221223.10920: *3* class SendThreaded
    class SendThreaded(threading.Thread):
        #@+others
        #@+node:amd_yen.20130429221223.10921: *4* __init__
        def __init__(self,email,passwd,to,subject,text):
            self.email = email
            self.passwd = passwd
            self.to = to
            self.subject = subject
            self.text = text
            threading.Thread.__init__(self)
            self.start()
        #@+node:amd_yen.20130429221223.10922: *4* run
        def run(self):
            print(self.email+" "+self.passwd+" "+self.to+" "+self.subject+" "+self.text)
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = self.to
            msg['Subject'] = self.subject
            msg.attach(MIMEText(self.text))
            mailServer = smtplib.SMTP("smtp.gmail.com", 587)
            mailServer.ehlo()
            mailServer.starttls()
            mailServer.ehlo()
            mailServer.login(self.email,self.passwd)
            mailServer.sendmail(self.email,self.to, msg.as_string())
            mailServer.close()
        #@-others
    #@+node:amd_yen.20130429221223.10923: *3* __init__
    def __init__(self,myemail,mypasswd):
        self.myemail = myemail
        self.mypasswd = mypasswd
    #@+node:amd_yen.20130429221223.10924: *3* sendMail
    def sendMail(self,to,subject,text):
        print(self.myemail+"\n")
        print(self.mypasswd+"\n")
        self.SendThreaded(self.myemail,self.mypasswd,to,subject,text)
    #@-others
#@-others
#@-leo

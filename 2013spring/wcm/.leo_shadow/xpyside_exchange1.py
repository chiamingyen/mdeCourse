#@+leo-ver=4-thin
#@+node:amd_yen.20130503085936.2409:@shadow wcm/pyside_exchange1.py
#encoding: utf-8
import sys
import locale
import urllib.request as urllib2
'''
若是採用 PyQt 則以下兩行取代 PySite 模組導入
from PyQt4.QtCore import *
from PyQt4.QtGui import *
'''
from PySide.QtCore import *
from PySide.QtGui import *
# 以下為 Wordpress 送資料所需模組
import xmlrpc.client
import datetime
import os

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        date = self.getdata()
        rates = sorted(self.rates.keys())
        
        # 與 wordpess 有關的成員變數
        self.wpsite = "http://wordpress.2012c1.hostingsiteforfree.com/xmlrpc.php"
        self.wpaccount = "account"
        self.wppass = "password"

        self.wptitle = "利用 Python 送資料"
        self.wpcontent = "這是以 Python 程式新增的網誌內容!\n並且進行跳行\n前面這裡跳行.<!--more-->在字串中嵌入內容"
        self.wpcontent +='''<pre lang="python" line="1" colla="+">'''
        self.wpcontent +='''這是註解中的內容'''
        self.wpcontent +='''</pre>'''

        self.wpcategory = ["Uncategorized"]
        self.keywords = ["python", "測試"]

        dateLabel = QLabel(date)
        self.fromComboBox = QComboBox()
        self.fromComboBox.addItems(rates)
        self.fromSpinBox = QDoubleSpinBox()
        self.fromSpinBox.setRange(0.01, 10000000.00)
        self.fromSpinBox.setValue(1.00)

        self.toComboBox = QComboBox()
        self.toComboBox.addItems(rates)
        self.toLabel = QLabel("1.00")
        # 加上一個 send wordpress 按鈕
        self.sendWp = QPushButton("&Send WP")

        grid = QGridLayout()
        grid.addWidget(dateLabel, 0, 0)
        grid.addWidget(self.fromComboBox, 1, 0)
        grid.addWidget(self.fromSpinBox, 1, 1)

        grid.addWidget(self.toComboBox, 2, 0)
        grid.addWidget(self.toLabel, 2, 1)
        # 放入 sendWp
        grid.addWidget(self.sendWp, 2, 2)

        self.setLayout(grid)

        self.connect(self.fromComboBox,
            SIGNAL("currentIndexChanged(int)"), self.updateUi)
        self.connect(self.toComboBox,
            SIGNAL("currentIndexChanged(int)"), self.updateUi)
        self.connect(self.fromSpinBox,
            SIGNAL("valueChanged(double)"), self.updateUi)
        # 連結 sendWp 按鈕與回呼函式
        self.sendWp.clicked.connect(self.newPost)

        self.setWindowTitle("Currency")

    def updateUi(self):
        to = self.toComboBox.currentText()
        from_ = self.fromComboBox.currentText()
        amount = (self.rates[from_] / self.rates[to]) * \
                 self.fromSpinBox.value()
        self.toLabel.setText(locale.format("%0.2f", \
            amount, True))

    def getdata(self): # Idea taken from the Python Cookbook
        self.rates = {}
        try:
            date = "Unknown"
            fh = urllib2.urlopen("http://www.bankofcanada.ca/en/markets/csv/exchange_eng.csv")
            for line in fh:
                line = line.rstrip().decode("UTF-8")
                if not line or line.startswith(("#", \
                    "Closing ")):
                    continue
                fields = line.split(",")
                if line.startswith("Date "):
                    date = fields[-1]
                else:
                    try:
                        value = float(fields[-1])
                        self.rates[fields[0]] = value
                    except ValueError:
                        pass
            self.rates["Canadian Dollar"] = 1.00
            return "Exchange Rates Date: " + date
        except Exception as e:
           return "Failed to download:\n%s" % e

    def newPost(self):
        wpsite = self.wpsite
        wpaccount = self.wpaccount
        wppass = self.wppass
        wptitle = "測試由 pyside 發布"
        wpcontent = self.wpcontent
        wpcategory = self.wpcategory
        keywords = self.keywords
        os.environ['TZ'] = 'Asia/Taipei'
        wp_blogid = "0"
        status_draft = 0
        status_published = 1
        server = xmlrpc.client.ServerProxy(wpsite)
        # 指定時間出版
        #date_created = xmlrpc.client.DateTime(datetime.datetime.strptime("2013-01-01 00:00", "%Y-%m-%d %H:%M"))
        # 以現在時間出版, 考慮與 Server 時間差八個小時 (480 分鐘), 因此要在 8 個小時前發表
        posttime = xmlrpc.client.DateTime(datetime.datetime.strptime((datetime.datetime.now()-datetime.timedelta(minutes=480)).strftime('%Y-%m-%d %H:%M'),"%Y-%m-%d %H:%M"))
        postdata = {'title': wptitle, 'description': wpcontent, 'dateCreated': posttime, 'categories': wpcategory, 'mt_keywords': keywords}
        # 將發布內容送出
        post_id = server.metaWeblog.newPost(wp_blogid, wpaccount, wppass, postdata, status_published)
        print("id:", post_id, " 已經登錄!")

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
#@-node:amd_yen.20130503085936.2409:@shadow wcm/pyside_exchange1.py
#@-leo

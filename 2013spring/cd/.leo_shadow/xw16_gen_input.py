#@+leo-ver=4-thin
#@+node:kmolII_lite.20130614201704.3064:@shadow cd/w16_gen_input.py
#@@language python

#coding: utf-8
# 利用程式產生輸入檔案
'''
馬達馬力     馬達轉速     齒輪減速比     齒形       安全係數      材料     小齒輪齒數
100           1200             4         type1          3        G10100_CD    18
150           2200             4         type4          3.2     G10100_CD    20
300           3200             3.5      type3          4        G10100_CD    25

馬達馬力: 100 ~ 1000
馬達轉速: 1000 ~ 3000
減速比:  1.5 ~ 4.5
齒形: type1 ~ type4
安全係數: 1.5 ~ 4.5
材料: 由資料庫中, 以亂數選擇一種
小齒輪齒數: 18 ~ 80
'''
import random
import optparse
from pybean import Store, SQLiteWriter

重複次數 = 250

# 此亂數產生函式是否比 random.randint(起頭, 結束) 更好?
def dice(num):
    parser = optparse.OptionParser()
    (options, args) = parser.parse_args()
    if not args:
        args = [1]
    for dieCount in args:
        dieCount = int(dieCount)
        total = 0
        dice = []
        for counter in range(dieCount):
            die = random.randrange(num)+1
            total = total + die
            dice.append(die)
    return total

def myrand(start, end):
    start = start - 1
    return start+dice(end-start)

# 在起頭與結束範圍內, 以亂數傳回馬達馬力的函式
def 馬達馬力(起頭, 結束):
    #產生數字 = random.randint(起頭, 結束)
    產生數字 = myrand(起頭, 結束)
    return 產生數字

def 馬達轉速(起頭, 結束):
    #產生數字 = random.randint(起頭, 結束)
    產生數字 = myrand(起頭, 結束)
    return 產生數字

def 減速比(起頭, 結束):
    #產生數字 = random.randint(起頭, 結束)
    產生數字 = myrand(起頭, 結束)
    return 產生數字*1.5

def 齒形(起頭, 結束):
    #產生數字 = random.randint(起頭, 結束)
    產生數字 = myrand(起頭, 結束)
    return 產生數字

def 安全係數(起頭, 結束):
    #產生數字 = random.randint(起頭, 結束)
    產生數字 = myrand(起頭, 結束)
    return 產生數字*1.5

def 材料(序號):
    # 根據資料庫查詢傳回對應的材料 unsno 與 treatment
    # 利用 Store  建立資料庫檔案對應物件, 並且設定 frozen=True 表示不要開放動態資料表的建立
    SQLite連結 = Store(SQLiteWriter("lewis.db", frozen=True))
    material = SQLite連結.find_one("steel","serialno = ?",[序號])
    # 針對 material.treatment 中的空白與 big5 資料進行處理
    treatment = material.treatment.replace(" ", "_")
    data = str(material.unsno)+"_"+str(treatment)
    # 以下的 split() 目的在測試如何分割 unsno 與 treatment
    # 只針對第一個底線進行分割
    unsno, treatment = data.split("_", 1)
    return unsno+"_"+treatment

def 小齒輪齒數(起頭, 結束):
    產生數字 = random.randint(起頭, 結束)
    return 產生數字

# 產生次序檔案, 內容採用 UTF-8 編碼
檔案 = open("design_input.txt", "w", encoding="UTF-8")
輸入行 = ""
for 索引 in range(重複次數):
    輸入行 += str(馬達馬力(100, 1000))
    輸入行 +="\t"
    輸入行 += str(馬達轉速(1000, 3000))
    輸入行 +="\t"
    輸入行 += str(減速比(1, 3))
    輸入行 +="\t"
    輸入行 += str(齒形(1, 4))
    輸入行 +="\t"
    輸入行 += str(安全係數(1, 3))
    輸入行 +="\t"
    # 產生材料資料序號亂數
    #材料序號 = random.randint(1, 70)
    材料序號 = myrand(1, 70)
    輸入行 += str(材料(材料序號))
    輸入行 +="\t"
    輸入行 += str(小齒輪齒數(18, 80))
    輸入行 +="\t"
    檔案.write(輸入行+"\n")
    # 每寫入一行後, 輸入行要 reset
    輸入行 = ""
檔案.close()

#@-node:kmolII_lite.20130614201704.3064:@shadow cd/w16_gen_input.py
#@-leo

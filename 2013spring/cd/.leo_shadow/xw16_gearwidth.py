#@+leo-ver=4-thin
#@+node:kmolII_lite.20130614201704.3065:@shadow cd/w16_gearwidth.py
#@@language python

#coding: utf-8
'''
"本程式的目的在輔助設計者選擇齒輪的尺寸大小，";
"由於相囓合的兩齒輪其徑節 (Diametral Pitch) 相同";
"，齒的大小也相同。因徑節為每單位直徑的齒數，因此徑節愈大，則其齒的尺寸愈小";
"；反之，徑節愈小，則齒的尺寸則愈大。";
"一般在設計齒輪對時，為避免使用過大的齒及過寬的齒面厚度，因此必須要就齒輪大小與強度與負載加以設計。";
"一般而言是希望齒輪面的寬度 (Face Width) 能大於3倍周節 (Circular Pitch)，以避免選用太大的齒尺寸。";
"並且希望齒輪面的寬度 (Face Width) 能小於5倍周節，以便齒面傳遞負載時能有較為均勻的分佈，因此";
"設 d 為齒輪的節圓直徑(Pitch Diameter)，單位為英吋";
"N 為齒數";
"P 為徑節， 即單位英吋的齒數";
"因此 d=N/P";
"設 V 為節線速度(Pitch Line Velocity)，單位為英呎/分鐘";
"因此 V=(PI) * d * n/12";
"其中 n 為齒輪轉速，單位為 rpm";
"設傳輸負載大小為 W，單位為 pounds";
"因此 W=33000H/V";
"其中 H 為傳輸功率，單位為 hourse power";
"若設 K 為速度因子(Velocity Factor)";
"因此 K=1200/(1200+V)";
"最後可求出齒輪的齒面寬度(Face Width) F ，單位為英吋";
"即 F=WP/KYS";
"其中 S 為齒面的材料彎曲應力強度";
"設計要求:控制所選齒的尺寸大小，在滿足強度與傳輸負載的要求下，讓齒面厚度介於3倍周節與5倍周節之間。";
"設計者可以選擇的參數:";
"安全係數(建議值為3以上)";
"齒輪減速比";
"馬達傳輸功率，單位為 horse power";
"馬達轉速，單位為 rpm";
"齒制(Gear System)";
"齒輪材料與強度";
'''
# 這個程式要計算正齒輪的齒面寬, 資料庫連結希望使用 pybean 與 SQLite
# 導入 pybean 模組與所要使用的 Store 及 SQLiteWriter 方法
from pybean import Store, SQLiteWriter
import math

# 執行 formfactor 內插運算的函式
def interpolation(小齒輪齒數, 齒形):
    global SQLite連結
    # 使用內插法求值
    # 找出比目標齒數大的其中的最小的,就是最鄰近的大值
    lewis_factor = SQLite連結.find_one("lewis","gearno > ?",[小齒輪齒數])
    if(齒形 == 1):
        larger_formfactor = lewis_factor.type1
    elif(齒形 == 2):
        larger_formfactor = lewis_factor.type2
    elif(齒形 == 3):
        larger_formfactor = lewis_factor.type3
    else:
        larger_formfactor = lewis_factor.type4
    larger_toothnumber = lewis_factor.gearno

    # 找出比目標齒數小的其中的最大的,就是最鄰近的小值
    lewis_factor = SQLite連結.find_one("lewis","gearno < ? order by gearno DESC",[小齒輪齒數])
    if(齒形 == 1):
        smaller_formfactor = lewis_factor.type1
    elif(齒形 == 2):
        smaller_formfactor = lewis_factor.type2
    elif(齒形 == 3):
        smaller_formfactor = lewis_factor.type3
    else:
        smaller_formfactor = lewis_factor.type4
    smaller_toothnumber = lewis_factor.gearno
    calculated_factor = larger_formfactor + (小齒輪齒數 - larger_toothnumber) * 
    (larger_formfactor - smaller_formfactor) / (larger_toothnumber - smaller_toothnumber)
    # 只傳回小數點後五位數
    return round(calculated_factor, 5)

# 取得設計參數
馬力 = 100
轉速 = 1120
減速比 = 4
齒形 = 4
安全係數 = 3
#unsno_treatment
材料 = "G10350_CD"
小齒輪齒數 = 18

# 改寫為齒面寬的設計函式
def gear_width(馬力, 轉速, 減速比, 齒形, 安全係數, 材料, 小齒輪齒數):
    # 根據所選用的齒形決定壓力角
    if(齒形 == 1 or 齒形 == 2):
        壓力角 = 20
    else:
        壓力角 = 25

    # 根據壓力角決定最小齒數
    if(壓力角== 20):
        最小齒數 = 18
    else:
        最小齒數 = 12

    # 直接設最小齒數
    if 小齒輪齒數 <= 最小齒數:
        小齒輪齒數 = 最小齒數
    # 大於400的齒數則視為齒條(Rack)
    if 小齒輪齒數 >= 400:
        小齒輪齒數 = 400

    # 根據所選用的材料查詢強度值
    # 由 material之序號查 steel 表以得材料之降伏強度S單位為 kpsi 因此查得的值要成乘上1000
    # 利用 Store  建立資料庫檔案對應物件, 並且設定 frozen=True 表示不要開放動態資料表的建立
    SQLite連結 = Store(SQLiteWriter("lewis.db", frozen=True))
    # 指定 steel 資料表
    steel = SQLite連結.new("steel")
    # 資料查詢
    # 將 unsno 與 treatment 從材料字串中隔開
    unsno, treatment = 材料.split("_")
    #print(unsno, treatment)

    material = SQLite連結.find_one("steel","unsno=? and treatment=?",[unsno, treatment])
    # 列出 steel 資料表中的資料筆數
    #print(SQLite連結.count("steel"))
    print (material.yield_str)
    strengthstress = material.yield_str*1000
    # 由小齒輪的齒數與齒形類別,查詢lewis form factor
    # 先查驗是否有直接對應值
    on_table = SQLite連結.count("lewis","gearno=?",[小齒輪齒數])
    if on_table == 1:
        # 直接進入設計運算
        print("直接運算")
        print(on_table)
        lewis_factor = SQLite連結.find_one("lewis","gearno=?",[小齒輪齒數])
        #print(lewis_factor.type1)
        # 根據齒形查出 formfactor 值
        if(齒形 == 1):
            formfactor = lewis_factor.type1
        elif(齒形 == 2):
            formfactor = lewis_factor.type2
        elif(齒形 == 3):
            formfactor = lewis_factor.type3
        else:
            formfactor = lewis_factor.type4
    else:
        # 沒有直接對應值, 必須進行查表內插運算後, 再執行設計運算
        print("必須內插")
        #print(interpolation(小齒輪齒數, 齒形))
        formfactor = interpolation(小齒輪齒數, 齒形)

    # 開始進行設計運算

    ngear = 小齒輪齒數 * 減速比

    # 重要的最佳化設計---儘量用整數的diametralpitch
    # 先嘗試用整數算若 diametralpitch 找到100 仍無所獲則改用 0.25 作為增量再不行則宣告 fail
    counter = 0
    i = 0.1
    facewidth = 0
    circularpitch = 0
    while (facewidth <= 3 * circularpitch or facewidth >= 5 * circularpitch):
        diametralpitch = i
        #circularpitch = 3.14159/diametralpitch
        circularpitch = math.pi/diametralpitch
        pitchdiameter = 小齒輪齒數/diametralpitch
        #pitchlinevelocity = 3.14159*pitchdiameter*轉速/12
        pitchlinevelocity = math.pi * pitchdiameter * 轉速/12
        transmittedload = 33000 * 馬力/pitchlinevelocity
        velocityfactor = 1200/(1200 + pitchlinevelocity)
        # formfactor is Lewis form factor
        # formfactor need to get from table 13-3 and determined ty teeth number and type of tooth
        # formfactor = 0.293
        # 90 is the value get from table corresponding to material type
        facewidth = transmittedload * diametralpitch * 安全係數/velocityfactor/formfactor/strengthstress
        if(counter>5000):
            print("超過5000次的設計運算,仍無法找到答案!")
            print("可能所選用的傳遞功率過大,或無足夠強度的材料可以使用!")
            # 離開while迴圈
            break
        i += 0.1
        counter += 1
    facewidth = round(facewidth, 4)
    if(counter<5000):
        print("進行"+str(counter)+"次重複運算後,得到合用的facewidth值為:"+str(facewidth))

# 執行正齒輪齒面寬的設計運算
gear_width(馬力, 轉速, 減速比, 齒形, 安全係數, 材料, 小齒輪齒數)

# 執行輸入檔案的解讀

# 取得各行輸入值後, 再呼叫 gear_width 執行齒面寬的設計運算
#@-node:kmolII_lite.20130614201704.3065:@shadow cd/w16_gearwidth.py
#@-leo

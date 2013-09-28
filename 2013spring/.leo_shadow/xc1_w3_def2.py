#@+leo-ver=4-thin
#@+node:cmsxh.20130928094546.3010:@shadow c1_w3_def2.py
#@@language python

def 增量列印(行數):
    # 基本的 print() 函式列印
    # 只要將 4 改為 11, 就可以重複列印 10 行
    #for 列印行數 in range(1, 4):
    for 列印行數 in range(1, 行數+1):
        print("Welcome to Python3 ", end="")
        for 列印個數 in range(列印行數):
            print("*", end="")
        # 完成多星號列印後, 必須額外要求跳行, 否則各行會列在同一行
        print()
        
def 減量列印(行數):
    # 將 step 設為 -1, 表示要從行數逐步減量
    # 為了配合增量列印達到個數最大值, 減量從 行數-1 開始
    for 列印行數 in range(行數-1, 0, -1):
        print("Welcome to Python3 ", end="")
        for 列印個數 in range(列印行數):
            print("*", end="")
        # 完成多星號列印後, 必須額外要求跳行, 否則各行會列在同一行
        print()
        
''' 完成初步增量與減量列印測試後, 再將此兩函式納入第三個函式當中
增量列印(10)
減量列印(10)
'''
def 增減量列印(最大行數):
    增量列印(最大行數)
    減量列印(最大行數)

增減量列印(10)
#@nonl
#@-node:cmsxh.20130928094546.3010:@shadow c1_w3_def2.py
#@-leo

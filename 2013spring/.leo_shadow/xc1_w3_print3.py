#@+leo-ver=4-thin
#@+node:cmsxh.20130928094546.3006:@shadow c1_w3_print3.py
#@@language python

# 基本的 print() 函式列印
# 只要將 4 改為 11, 就可以重複列印 10 行
for 列印行數 in range(1, 4):
    print("Welcome to Python3 ", end="")
    for 列印個數 in range(列印行數):
        print("*", end="")
    # 完成多星號列印後, 必須額外要求跳行, 否則各行會列在同一行
    print()
#@-node:cmsxh.20130928094546.3006:@shadow c1_w3_print3.py
#@-leo

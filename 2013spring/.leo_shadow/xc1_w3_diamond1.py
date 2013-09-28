#@+leo-ver=4-thin
#@+node:cmsxh.20130928094546.3002:@shadow c1_w3_diamond1.py
#@@language python

# 本程式在 demo
# print()
# def
# range()
# list()
# list 內容變化
# reversed()
# zip()
# if elif else

def 列印星號(輸入變數):
    數列1 = list(range(輸入變數))
    數列2 = [x+輸入變數-1 for x in 數列1]
    反數列2 = reversed(數列1)
    集合 = zip(數列2, 反數列2)
    for 索引 in 集合:
        for 數 in range(輸入變數*2):
            if 數 == 索引[0] or 數 == 索引[1]:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def 列印星號2(輸入變數):
    數列1 = list(range(輸入變數))
    數列2 = [x+輸入變數 for x in 數列1]
    數列3 = [x+1 for x in 數列1]
    反數列2 = reversed(數列2)
    集合 = zip(數列3, 反數列2)
    for 索引 in 集合:
        for 數 in range(輸入變數*2):
            if 數 == 索引[0] or 數 == 索引[1]:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def 列印星號3(輸入變數):
    數列1 = list(range(輸入變數))
    數列2 = [x+輸入變數-1 for x in 數列1]
    反數列2 = reversed(數列1)
    集合 = zip(數列2, 反數列2)
    for 索引 in 集合:
        for 數 in range(輸入變數*2-1):
            if 數 <= 索引[0] and 數 >= 索引[1]:
                print("2", end="")
            else:
                print("1", end="")
        print()

def 列印星號4(輸入變數):
    數列1 = list(range(輸入變數))
    數列2 = [x+輸入變數 for x in 數列1]
    數列3 = [x+1 for x in 數列1]
    反數列2 = reversed(數列2)
    集合 = zip(數列3, 反數列2)
    for 索引 in 集合:
        for 數 in range(輸入變數*2+1):
            if 數 >= 索引[0] and 數 <= 索引[1]:
                print("2", end="")
            else:
                print("1", end="")
        print()

def 列印菱形(輸入變數):
    列印星號3(輸入變數)
    列印星號4(輸入變數-1)

列印菱形(11)

# 請將本程式改為菱形中間也要列印星號
#@nonl
#@-node:cmsxh.20130928094546.3002:@shadow c1_w3_diamond1.py
#@-leo

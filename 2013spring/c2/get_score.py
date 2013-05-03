#encoding: utf-8
'''這個程式將配合 TCExam 所轉出來的 txt 成績檔案, 以遞迴方式讀取檔案
並將要取出的資料存入資料庫中
'''
import os, fnmatch
# 導入 pybean 模組與所要使用的 Store 及 SQLiteWriter 方法
from pybean import Store, SQLiteWriter
# 利用 Store  建立資料庫檔案對應物件, 並且設定 frozen=False 表示要開放動態資料表的建立
library = Store(SQLiteWriter("2013exam.sqlite", frozen=False))

# 定義一個可以遞迴進入目錄搜尋特定檔案的函式
def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename

 # 定義一個讀取檔案所有內容的函式
def read_lines(input_filename):
    output_list = []
    f = open(input_filename, encoding="UTF-8")
    while True:
        l = f.readlines()
        if len(l) == 0:
            break
        output_list.append(l)
    f.close()
    return output_list

if __name__ == '__main__':
    # mylist 為各檔案內容
    mylist = []
    # finallist 為最後擷取出來的資料內容
    finallist = []
    # 分別取得檔案名稱
    for filename in find_files('./', '*.txt'):
        # we go through all the files, and read file content in to my list
        mylist = read_lines(filename)
        # mylist 為各檔案中的所有資料
        # 取各檔案的各行內容, mylist[myindex]
        for myindex in range(len(mylist)):
            for lineindex in range(len(mylist[myindex])):
                # yes we print line by line for each file
                mycolumn = ((mylist[myindex][lineindex]).rstrip()).split('\t')
                # only list the first column is digit
                if mycolumn[0].isdigit():
                    #mycolumn[6] 為學號
                    # mycolumn[8] 為成績
                    course_title = filename.split('\\')[0][2:]
                    exam_title = filename.split('\\')[1]
                    # 動態建立 book 資料表
                    score = library.new("score")
                    score.title = course_title
                    score.exam = exam_title
                    score.student = mycolumn[6]
                    score.points = mycolumn[8]
                    library.save(score)
                    library.commit()
                    finallist.append([course_title, exam_title, mycolumn[6],mycolumn[8]])
                    #print(course_title,":", exam_title, ":", mycolumn[6],":",mycolumn[8])

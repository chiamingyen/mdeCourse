#encoding: utf-8
from get_score import *
from pybean import Store, SQLiteWriter

library = Store(SQLiteWriter("2013exam.sqlite", frozen=False))

def get_studid(filename, course_title, count):
    print(course_title)
    fail = 0
    student_list = read_lines(filename)
    for 索引 in range(len(student_list[0])):
        item = None
        student_id = ((student_list[0][索引]).rstrip()).split('\t')[0]
        score = get_score(course_title, student_id)
        total = 0
        average = 0
        for item in score:
            points = float(item.points)
            if points < 0:
                points = 0
            total += points
            #print(item.student, item.title, item.exam, item.points)
        # 假設大家都 100 分
        期中報告成績 = 100
        報告比例 = 0.2
        考試比例 = 0.8
        #(分組加分)
        全班加分 = 2

        期中成績 = int((total/count)*考試比例+(期中報告成績*報告比例)+全班加分)
        if item != None:
            if 期中成績 < 60:
                fail +=1
                print(">",item.student,":", 期中成績)
            else:
                if 期中成績 > 99:
                    期中成績 = 99
                print(item.student,":", 期中成績)
        else:
            fail +=1
            print(student_id, ":", "沒有資料")
    print("不及格人數:", fail)
    print("##################")

def get_score(course_title, student_id):
    score = library.find("score","title=? and student=?",[course_title, student_id])
    return score

# 修課學員名單為 list_c2.stud, 考試名稱為 c2_exam, 總共考了 4 次考試
get_studid('list_c2.stud', 'c2_exam', 4)
get_studid('list_wcm.stud', 'wcm_exam', 3)
get_studid('list_cda.stud', 'cda_exam', 3)
get_studid('list_cdb.stud', 'cdb_exam', 3)


//--------------- 程式 5.1 ------------------

/* 程式 5.1 from PTRTUT10.HTM     6/13/97 */
#include <stdio.h>
#include <string.h>
struct tag {
    char lname[20];      /* 姓 */
    char fname[20];      /* 名 */
    int age;             /* 年齡 */
    float rate;          /* 例如: 每小時 100 元 */
};
struct tag my_struct;       /* 宣告 my_struct　結構 */
int main(void)
{
    strcpy(my_struct.lname,"Jensen");
    strcpy(my_struct.fname,"Ted");
    printf("\n%s ",my_struct.fname);
    printf("%s\n",my_struct.lname);
    return 0;
}

//-------------- 結束程式 5.1 --------------

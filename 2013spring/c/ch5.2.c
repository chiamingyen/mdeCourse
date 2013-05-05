//------------ 程式 5.2 ---------------------

/* 程式 5.2 from PTRTUT10.HTM   6/13/97 */
#include <stdio.h>
#include <string.h>
struct tag{                     /* 結構型別 */
    char lname[20];             /* 姓 */
    char fname[20];             /* 名 */
    int age;                    /* 年齡 */
    float rate;                 /* 例如: 每小時 100 元 */
};
struct tag my_struct;           /* 結構定義 */
void show_name(struct tag *p);  /* 函式原型 */
int main(void)
{
    struct tag *st_ptr;         /* 指向結構的指標變數 */
    st_ptr = &my_struct;        /* 將指標指向 my_struct */
    strcpy(my_struct.lname,"Jensen");
    strcpy(my_struct.fname,"Ted");
    printf("\n%s ",my_struct.fname);
    printf("%s\n",my_struct.lname);
    my_struct.age = 63;
    show_name(st_ptr);          /* 輸入該指標 */
    return 0;
}
void show_name(struct tag *p)
{
    printf("\n%s ", p->fname);  /* p 指向結構 */
    printf("%s ", p->lname);
    printf("%d\n", p->age);
}

//-------------------- 結束程式 5.2 ----------------

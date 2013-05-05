//------------------program 3.1-------------------------------------

/* Program 3.1 from PTRTUT10.HTM   6/13/97 */

#include <stdio.h>

char strA[80] = "A string to be used for demonstration purposes";
char strB[80];

int main(void)
{

    char *pA;     /* 字元型別的指標變數*/
    char *pB;     /* 另一個字元型別的指標變數 */
    puts(strA);   /* 顯示字串 A */
    pA = strA;    /* 將 pA 指向字串 A*/
    puts(pA);     /* 顯示 pA 指向的內容 */
    pB = strB;    /* 將 pB 指向字串 B */
    putchar('\n');       /* 在螢幕中向下移動一行 */
    while(*pA != '\0')   /* A 行 (詳見內文說明) */
    {
        *pB++ = *pA++;   /* B 行 (詳見內文說明) */
    }
    *pB = '\0';          /* C 行 (詳見內文說明) */
    puts(strB);          /* 將 strB 顯示在螢幕上 */
    return 0;
}

//--------- end program 3.1 -------------------------------------

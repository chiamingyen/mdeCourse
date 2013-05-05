#include <stdio.h>

// 每一個 C 程式都必須要有一個小寫的 main()函式
int main()
{
    // 陣列與指標的應用
    char a[20];
    int i;
    a[3] = 'x';
    printf("%c\n",a[3]);
    printf("%c\n",3[a]);
    printf("%c\n",*(a+3));
    printf("%c\n",*(3+a));
    return 0;
}

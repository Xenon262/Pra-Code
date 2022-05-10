#include <stdio.h>

int main(){
    int a,b;

    printf("请输入任意两个整数：");
    scanf("%d %d",&a,&b);

    int max = 0;
    if (a > b)
    {
        max = a;
    }
    else if (a < b)
    {
        max = b;
    }
    else
    {
        max = a = b;
    }
    
    printf("最大的数字是%d",max);

    return 0;
}
#include <stdio.h>

int main(){
    int price = 0;
    
    printf("请输入金额（元）：");
    // 要求scanf这个函数读入下一个整数，读到的结果赋值给变量price
    // 小心price前面的“&”（详情见指针）
    scanf("%d",&price);

    int change = 100 - price;

    printf("找您%d元。",change);

    return 0;
}
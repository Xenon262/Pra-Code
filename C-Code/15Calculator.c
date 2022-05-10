#include <stdio.h>

int main(){
    int price = 0,bill = 0;

    printf("请输入物品金额（元）：");
    scanf("%d",&price);
    printf("请输入票面：");
    scanf("%d",&bill);

    if (bill >= price)
    {
        printf("应该找您%d元。",bill-price);
    }
    else
    {
        printf("对不起，您的钱不够。");
    }
    return 0;
}
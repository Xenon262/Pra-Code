#include <stdio.h>

int main(){
    int price = 0;
    // 更好的方式，是定义一个常量，例如：const int AMOUNT = 100；
    // const是一个修饰符，被const修饰的变量一旦初始化，就不能再修改了
    const int AMOUNT = 100;

    printf("请输入金额（元）：");
    scanf("%d",&price);
    // 固定不变的数，叫做常数。直接写在程序里，称作直接量（literal）
    int change = AMOUNT - price;
    // int change = 100 - price;

    printf("找您%d元。",change);

    return 0;
}
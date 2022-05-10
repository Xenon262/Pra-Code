#include <stdio.h>

int main(void){
    // 表达式：一个表达式是一系列运算符和算子的组合，用来计算一个值
    // 运算符：指进行运算的动作，比如加法运算符“+”，减法运算符“-”
    // 算子：指参与运算的值，这个值可能是常数，也可能是变量，还可能是一个方法的返回值
    // 例如：a = b + 5。其中的a，b，5都是算子，=与+都是运算符

    // 例题：输入两个时间，每个时间分别输入小时和分钟的值，然后输出两个时间的差，以几小时几分表示
    int hour1,minute1;
    int hour2,minute2;

    scanf("%d %d",&hour1,&minute1);
    scanf("%d %d",&hour2,&minute2);

    int t1 = hour1 * 60 +minute1;
    int t2 = hour2 * 60 +minute2;

    if (t1 > t2)
    {
        int t = t1 -t2;
        printf("时间差是%d小时%d分钟",t/60,t%60);
    }
    else
    {
        int t = t2 -t1;
        printf("时间差是%d小时%d分钟",t/60,t%60);
    }
    return 0;
}
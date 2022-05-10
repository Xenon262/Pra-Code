#include <stdio.h>

int main(void){
    // 写一个程序，输入两个整数，输出他们的平均值
    int a,b;
    scanf("%d %d",&a,&b);

    double c = (a + b) / 2;
    printf("%d和%d的平均值是%f\n",a,b,c);
    return 0;
}

// 赋值运算符：
//          a = b = 6 --> a = (b = 6)
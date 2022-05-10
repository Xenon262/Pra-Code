#include <stdio.h>

int main(void){
    // 复合赋值：5个算术运算符“+ - * / %”与赋值运算符结合起来，形成复合赋值运算符：“+= -= *= /= %=”
    // 例如：a += 5;等于 a = a + 5;
    // 注意：两个运算符之间不能有空格

    // 递增递减运算符：“++” “--”
    // 作用是是给变量+1或-1
    // 例如：count++;等于count +=1;等于count = count + 1;
    // 前缀与后缀：a++ / ++a
    int a = 10;

    printf("a++=%d\n",a++);
    printf("a=%d\n",a);

    printf("++a=%d\n",++a);
    printf("a=%d\n",a);
    return 0;
}
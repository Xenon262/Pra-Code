#include <stdio.h>

int main(){
    printf("请分别输入身高的英尺和英寸，如输入\"5 7\"表示5英尺7英寸:");

    int foot;
    // int inch可换为double（双精度浮点数）或float（单精度浮点数）
    int inch;

    scanf("%d %d",&foot,&inch);
    // 浮点数：带小数点的数值
    printf("身高是%f米。\n",(foot+inch/12.0)*0.3048);

    return 0;
}

// 数据类型:
//          整数:int,printf("%d",...),scanf("%d",...)
//          带小数点的数:double,printf("%f",...),scanf("%lf",...)
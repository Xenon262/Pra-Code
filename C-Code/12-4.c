#include <stdio.h>

int main(void){
    int cm = 0;
    printf("请输入一串身高数字（单位厘米）：");
    scanf("%d",&cm);

    int foot = cm / 30.48;
    int inch = ((cm / 30.48) - foot) * 12;

    printf("%d",foot);
    printf("%d",inch);

    return 0;
}
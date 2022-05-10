#include <stdio.h>

int main(){

    const int PASS = 60;
    int score;

    printf("请输入你的成绩：");
    scanf("%d",&score);

    printf("你输入的成绩是：%d\n",score);
    if (score >= PASS)
    {
        printf("恭喜你，及格了！\n");
    }
    else
    printf("很遗憾，你没有及格。\n");
    
    printf("再见。");

    return 0;
}
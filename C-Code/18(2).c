#include <stdio.h>

int main(){
    const int READY = 24;
    int code,count;

    scanf("%d %d",&code,&count);
    if (code == READY)
        if(code < 20)
            printf("一切正常");
        else
            printf("继续等待");
            
    return 0;
}
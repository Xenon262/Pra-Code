#include <stdio.h>

int main(void){
    int a = 5;
    int b = 6;
    int t;

    t = a;
    a = b;
    b = t;

    printf("a=%d,b=%d\n",a,b);
    printf("t=%d",t);
    return 0; 
}
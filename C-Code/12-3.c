#include <stdio.h>

int main(void){
    int a;
    scanf("%d",&a);
    
    int a1 = a/100;
    int a2 = a%100/10;
    int a3 = a%100%10;

    printf("%d%d%d",a3,a2,a1);

    return 0;
}
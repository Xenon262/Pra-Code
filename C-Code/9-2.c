#include <stdio.h>

int main(void){
    // 例题：如果一年期的定期利率是3.3%，那么连续自动转存3年后，最初存入的X元定期会得到多少本息余额
    // 本息合计 = x(1+3.3%)^3

    int x;
    
    scanf("%d",&x);

    double amount = x * (1+0.033) * (1+0.033) * (1+0.033);
    printf("%f",amount);
    return 0;
}
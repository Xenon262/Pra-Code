#include <stdio.h>

int main(){
    // ==：相等     !=：不等于     >：大于     >=：大于等于     <：小于     <=：小于等于
    // 关系运算的结果为整数1，否则为整数0(成立为1,不成立为0)
    // printf("%d\n",3==2);
    // printf("%d\n",3>2);
    // printf("%d\n",3<=2);
    return 0;
}

// 所有关系运算符的优先级都比算术运算符低，但是比赋值运算的高
// 判断是否相等的==和!=的优先级比其他的低,而是连续的关系运算从左到右进行的
// 例如:5 > 3 == 6 > 4
    // 6 > 5 >4
    // a == b == 6
    // a == b > 0
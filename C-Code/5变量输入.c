#include <stdio.h>

int main(){
    int price = 0;
    
    printf("�������Ԫ����");
    // Ҫ��scanf�������������һ�������������Ľ����ֵ������price
    // С��priceǰ��ġ�&���������ָ�룩
    scanf("%d",&price);

    int change = 100 - price;

    printf("����%dԪ��",change);

    return 0;
}
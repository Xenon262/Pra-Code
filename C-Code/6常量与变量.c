#include <stdio.h>

int main(){
    int price = 0;
    // ���õķ�ʽ���Ƕ���һ�����������磺const int AMOUNT = 100��
    // const��һ�����η�����const���εı���һ����ʼ�����Ͳ������޸���
    const int AMOUNT = 100;

    printf("�������Ԫ����");
    scanf("%d",&price);
    // �̶��������������������ֱ��д�ڳ��������ֱ������literal��
    int change = AMOUNT - price;
    // int change = 100 - price;

    printf("����%dԪ��",change);

    return 0;
}
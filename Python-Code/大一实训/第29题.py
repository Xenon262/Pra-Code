x=int(input("请输入数字："))
m,n=1,0
while m<=x:
    if x%m==0:
        n+=1
    m+=1
if n>x:
    print("完全数")
elif n==x:
    print("丰沛数")
else:
    print("不足数")

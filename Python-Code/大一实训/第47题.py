a=int(input("请输入一个数字:"))
b=int(input("再输入一个数字:"))
m=[]
if a>b:
    smaller=b
else:
    smaller=a
for i in range(1,smaller+1):
    if(a%i==0)and(b%i==0):
        m.append(i)
        continue
n=m[-1]
print("%d和%d的最大公约数为:%d"%(a,b,n))
print("%d和%d的最小公倍数为:%d"%(a,b,a*b//n))

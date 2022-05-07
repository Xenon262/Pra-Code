a=int(input("请输入第一个数:"))
b=input("请输入操作符:")
c=int(input("请输入第二个数:"))
d=a+c
e=a-c
f=a*c
g=a/c
h="+"
i="-"
j="*"
k="/"
if b==h:
    print("输出为%s"%d)
elif b==i:
    print("输出为%s"%e)
elif b==j:
    print("输出为%s"%f)
elif b==k:
    print("输出为%s"%g)

import random
n=0
for i in range(10):
    x=random.randint(10,99)
    n=n+x
    print(x,end=" ")
    if i==0:
        max=x
    else:
        if x>max:
            max=x
    if i==0:
        min=x
    else:
         if x<min:
             min=x
    
print("\n最大值：",max)
print("\n最小值：",min)
print("\n平均值：",n/10)

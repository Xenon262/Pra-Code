x=0
print("1~1000内的全部素数有：")
for k in range(2,1001):
    for i in range(2,k):
        if k%i==0:
            break
    else:
        print(k,end=" ")
        x+=1
        if x%10==0:
            print()
print("\n共{}个。".format(x))

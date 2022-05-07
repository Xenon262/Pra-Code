x=0
for x in range(1000,10000):
    if x%7==0 and x%5!=0:
        print(x,end=" ")
        x+=1
        if x%10==0:
            print()

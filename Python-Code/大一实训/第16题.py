m=0
for i in range(1000,3001,2):
    print(i)
    if i%2==0:
        m+=1
print("偶数一共有{}个".format(m))
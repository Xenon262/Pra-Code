A=eval(input("输入A："))
B=eval(input("输入B："))
m=0
if A<-100 or A>B or B>100:
    print("输入错误!")
    
else:
    for i in range(A,B-1):
        A+=1
        m+=i
        print(A,end=" ")
    
   
print("\n和为{}".format(m))  

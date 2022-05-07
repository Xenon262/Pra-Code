a,b,c,d=1,0,0,0
while a<=1000:
    if a%2!=0:
        c+=a
    a+=1
while b<=1000:
    if b%2==0:
        d+=b
    b+=1
print("奇数和为{}，偶数和为{}".format(c,d))    

from random import *
checkcode=""
for i in range(4):
    x=randrange(0,4)
    if x!=i and x+1!=i:
        checkcode+=chr(randint(97,122)) 
    elif x+1==i:
        checkcode+=chr(randint(65,90))
    else:
        checkcode+=str(randint(1,9))
print("验证码:",checkcode)    
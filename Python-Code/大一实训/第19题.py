for i in range(400,501):
    n=1500-i
    if(n%3==2 and n%5==4 and n%7==6):
        print("剩下士兵{}人".format(n))
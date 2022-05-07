numlist=[]
i=1
def inputnum(num):
    numlist.append(num)
    return numlist

while 1==1:
    if i in range(1,11):
        a=int(input("请输入正整数："))
        inputnum(a)
        i+=1
    else:
        break
print("输入的数字依次为:")
print(numlist)
print("输入的数字由小到大依次为:")
numlist.sort()
print(numlist)

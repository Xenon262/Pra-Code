year = int(input('请输入年份：\t'))
month = int(input('请输入月份：\t'))
day=0
total=0
space=0
isRun = year%4==0 and year%100!=0 or year%400==0
for y in range(1900,year):
    if y%4==0 and y%100!=0 or y%400==0:
        total+=366
    else:
        total+=365
for m in range(1,month+1):
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        day=31
    elif m==2:
        if isRun==True:
            day=29
        else:
            day=28
    else:
        day=30
    if m<month:
        total+=day
space=total%7+1
if space==7:
    space=0
print('日\t一\t二\t三\t四\t五\t六')
for s in range(0,space):
    print('\t',end='')
for d in range(1,day+1):
    print('{}\t'.format(d),end='')
    if(total+d)%7==6:
         print('')

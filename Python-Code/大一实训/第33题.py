str_1=input("请输入一句话:")
str_2=str_1[::-1]
for i in range(len(str_1)):
    if str_1[i]==str_2[i]:
        i+=1
if i==len(str_1):
    print("是回文")
else:
    print("不是回文")

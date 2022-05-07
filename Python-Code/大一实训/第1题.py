x=float(input("你花费了:"))
print("最终花费了：",end=" ")
if x<1000:
    print(x)
elif 1000<=x<2000:
    print(0.9*x)
elif 2000<=x<3000:
    print(0.8*x)
else:
    print(0.7*x)
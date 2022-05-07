from math import *

x=int(input("请输入一个数："))
if x>5:
    print("y={}".format(sin(x)+sqrt(x**2+1)))
elif 0<x<=5:
    print("y={}".format(exp(x)+log(x,5)+pow(x,1/5)))
else:
    print("y={}".format((cos(x)-x**3+3*x)))

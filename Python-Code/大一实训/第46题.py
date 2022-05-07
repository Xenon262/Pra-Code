for i in range(1,23):
    if i<=11:
        print(" "*(i),end=" ""*"*(12-i))
        print()
    elif i==12:
        print(" "*(i-1),end=" ""*"*(i-11))
        print()
    else:
        print(" "*(23-i),end=" ""*"*(i-11))
        print()

month=int(input("month:"))
season=[[11,12,1,2],[3,4],[5,6,7,8],[9,10]]

if month in season[0][0:4]:
    print("winter")
elif month in season[1][0:2]:
    print("spring")
elif month in season[2][0:4]:
    print("summer")
elif month in season[3][0:2]:
    print("fall")
else:
    print("not regular month")

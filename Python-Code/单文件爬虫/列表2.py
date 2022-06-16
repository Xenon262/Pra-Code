print("2017~2018赛季NBA西部联盟前八名\n")
team = ["火箭","勇士","开拓者","雷霆","爵士","鹈鹕","马刺","森林狼"]
for index,item in enumerate(team):
    if index%2 == 0:           #判断是否为偶数，为偶数时不换行
        print(item + "\t\t",end='')
    else:
        print(item + '\n')    #换行输出
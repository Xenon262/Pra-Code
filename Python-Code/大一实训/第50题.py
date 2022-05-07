enrollment=0
for attendess in range(10):
    sex=input("请输入性别(男m,女f):")
    age=int(input("请输入年龄:"))
    if sex=="m":
        print("对不起只有10——12岁之间女孩可以参加")
    else:
        if age <10 or age >12:
            print("对不起只有10——12岁之间女孩可以参加")
        else:
            enrollment+=1
            print("欢迎加入球队")
print("满足人数:",enrollment)

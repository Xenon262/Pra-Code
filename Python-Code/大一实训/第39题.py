username=input("请输入您的用户名:")
password=input("请输入您的密码:")
if username=="admin":
    if password=="111111":
        print("输入正确，恭喜进入！")
    else:
        print("输入错误，请重试！")
else:
    print("用户名输入错误，请重试！")

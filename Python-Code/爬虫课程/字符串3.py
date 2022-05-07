str = '@明日科技 @扎克伯格 @俞洪敏'
list = str.split(' ')
print('您@的好友有：')
for item in list:
    print(item[1:])
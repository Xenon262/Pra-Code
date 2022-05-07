programmer_1 = '你知道我的生日吗'
print('程序员甲说：' + programmer_1)
programmer_2 = '输入你的身份证号'
print('程序员乙说：' + programmer_2)
idcard = '123456199006277890'
print('程序员甲说：' + idcard)
birthday = idcard[6:10] + '年' + idcard[10:12] + '月' + idcard[12:14] + '日'
print('程序员乙说：你是' + birthday + '出生的，所以你的生日是' + birthday[5:])
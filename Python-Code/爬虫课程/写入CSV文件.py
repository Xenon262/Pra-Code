import csv

data = [['姓名','性别','生日'],['小明','男','2016-06-06']]
with open('data.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    writer.writerow(['小红','女','2020-1-1'])
list = ['天天向上', '天上人间', '天空之城', '天龙八部']
for i in list:
    print(i)

# 切片
motto = '天天向上，天上人间，天空之城，天龙八部'
num = len(motto)
print(motto[0:num+1:2])
# 下标从0开始，到哪结束+1，2指隔一个取一个
print(motto[5:9])
print(motto[-4:-1])
print(motto[-4:])
print('地'+motto[1:])

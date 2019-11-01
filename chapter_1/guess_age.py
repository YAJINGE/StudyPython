# 设置目标年龄
guess_age = 32
# 如果3次以内猜中就是赢了
for guess_num in range(0,3):
    get_age = int(input('输入夏晶想要结婚的年龄(只有三次机会):'))
    if get_age == guess_age:
        print('恭喜你,你们很有缘哟!')
        break
    else:
        if 2-guess_num != 0:
            print('不好意思,没猜对哟,还有',2-guess_num,'次机会,请继续')
else:
    print('再接再厉吧')
print('game is over')
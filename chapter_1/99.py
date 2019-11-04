# 九九乘法表while循环
i = 1
# i 为行数
while i <= 9:
    j = 1
    # j 为列数
    while j <= i:
        # print(j, '*', i, '=', j * i,end='  ')
        print(f'{j}*{i}={j*i}',end='  ')
        j += 1
    print('\n')
    i += 1

# 九九乘法表for循环
for i in range(1,10):
    for j in range(1,i+1):
        print(j, '*', i, '=', j * i, end='  ')
    print('\n')
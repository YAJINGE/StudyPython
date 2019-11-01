import time
start = time.perf_counter() # 计算开始时间
'''
# for 循环
sum = 0
for i in range(0, 100000001):
    sum +=i
    # pass # 只执行循环
print(sum)
'''


# while循环
k = 0
sum1 = 0
while k <= 100000000:
    sum1 += k
    k += 1

print(sum1)
end = time.perf_counter() # 计算结束时间
print(start - end)
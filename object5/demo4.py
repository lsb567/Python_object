# 水仙花数：每个位置上的数的三次方相加等于这个数的值
import math
for i in range(100, 1000):
    if math.pow((i%10), 3) + math.pow((i//10%10), 3) + math.pow(i//100, 3) == i:
        print(i)
# 第一种方法
fp = open('D:/test.txt', 'w')
print('hello word', file=fp)
fp.close()

# 第二种方法
with open('D:/test1.txt', 'w') as file:
    file.write("hello wrod")
x = 97  # 代表的是a的ASCII值
for _ in range(1, 27):
    print(chr(x), '--->', x)
    x += 1

print('-------------------')
x = 97
while x <= 122:
    print(chr(x), '--->', x)
    x += 1
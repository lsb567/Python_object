constellation = ['1', '2', '3', '4', '5']
nature = ['11', '22', '33', '44', '55']

d = dict(zip(constellation, nature))
# for item in d:
#     print(item, d[item])
print(d)

key = input('请输入您的星座名称：')
flag = True
for item in d:
    if key == item:
        flag = True
        print(key, '的性格特点：', d.get(key))
        break
    else:
        # print('输入的星座有误')
        flag = False

if not flag:
    print('对不起，您输入的星座有误')


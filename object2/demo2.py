# 变量的赋值
name1 = '林黛玉'
name2 = '薛宝钗'
name3 = '贾元春'
name4 = '贾探春'
name5 = '史香玲'
print('➊\t'+name1)
print('➊\t'+name2)
print('➊\t'+name3)
print('➊\t'+name4)
print('➊\t'+name5)

# 第二种方式 列表
lst_name = ['灵代玉', '薛宝钗', '贾元春', '贾探春', '史湘云']
lst_sig = ['➊']
for i in range(5):
    print(lst_name[i], lst_sig[0])

# 第三种方式 字典
d = {'➊': '林黛玉'}
print('--------------------')
for key in d:
    print(key, d[key])
print('zip-------------------')
for s, name in zip(lst_sig, lst_name):
    print(s, name)
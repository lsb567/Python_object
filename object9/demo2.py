def show(lst):
    for item in lst:
        for i in item:
            print(i, end='\t\t')
        print()  # 换行

lst = [
    ['01', '电风扇', '美的', 500],
    ['02', '洗衣机', 'tcl', 400],
    ['03', '微波炉', '老板', 400],
]
print('编号\t名称\t\t品牌\t\t单价')
show(lst)
print('---------------------')

for item in lst:
    item[0] = '0000' + item[0]
    item[3] = '￥{:.2f}'.format(item[3])

show(lst)
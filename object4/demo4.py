d = {
    '白羊座': '1fdsafdsafds',
    '金牛座': 'dfskdafjdsasdkf',
    '射手座': 'fkdsljafkdjsaklf'
}
star = input('请输入您的星座查看近来的运势：')
# print(d[star])
print(d.get(star))  # 及时获取不到你输入的值也不会报错

for i in range(1, 4):
    user_name = input('请输入用户名:')
    user_pwd = input('请输入密码:')
    if user_name == 'admin' and user_pwd == '8888':
        print('登录成功')
        break
    else:
        print('用户名或密码不正确')
        if i < 3:
            print(f'你还有{3 - i}次机会')
else:
    print('对不起，你没有机会了')
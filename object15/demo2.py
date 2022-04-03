def find_answer(question):
    with open('replay.txt', 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:  # if line == '' 到文件末尾
                break
            # 字符串的分割
            keyword = line.split('|')[0]
            reply = line.split('|')[1]
            if keyword in question:
                return reply

        return False


if __name__ == '__main__':
    question = input('嗨，您好，你有啥事？')
    while True:
        if question == 'bye':
            break
        # 开始在文件中查找
        replay = find_answer(question)
        if not replay:  # 如果回复的事False, not False-->True
            question=input('不知道你在说什么，你要问关于订单，物流，账户，支付等问题，（退出请输入bye）')
        else:
            print(replay)
            question = input('还有啥事？')
    print('再见')

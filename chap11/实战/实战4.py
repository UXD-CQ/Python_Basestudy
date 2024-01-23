'''
实战四:模拟淘宝客服自动回复
需求:淘宝客服为了快速回答买家问题,设置了自动回复的功能能,当有买家咨询时,客服自助系统会首先使用提前规划好的内容进行回复,请用Python程序实现这一功能
'''
def find_answer():
    with open('replay.txt', 'r', encoding='utf-8') as f:  
        while True:
            line = f.readline()
            if line=='':
                break # 退出while循环
            # 字符串的分割操作
            keyword=line.split('|')[0]
            reply=line.split('|')[1]
            if keyword in question:
                return reply
    return False

if __name__ == '__main__':
    question = input('嗨，XXX您好！请输入您的问题:')
    while True:
        if question == 'bye':
            break
        else:
            # 开始查找要回复的答案
            reply = find_answer(question)
            if reply==False: # 如果函数的返回值是False
                question=input('抱歉，我暂时无法回答您的问题，请重新输入(订单、物流、账户、支付)问题，退出请输入bye:')
            else:
                print(reply)
                question=input('嗨，XXX您好！请输入您的(订单、物流、账户、支付)问题:')
    print('再见，祝您生活愉快！')
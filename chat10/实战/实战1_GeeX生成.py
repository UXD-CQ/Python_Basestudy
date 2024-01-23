'''
实战一:模拟高铁售票系统
需求:假设高铁一节车厢的座位数有6行,每行5列,每个座位初始显
示"有票",用户输入座位位置(如,4,3)后,按回车,则该座位
显示为"已售",使用到第三方模块prettytable
'''
import prettytable as pt
def init_table():
    ticket = [['有票' for i in range(5)] for j in range(6)]
    return ticket

def show_table(ticket):
    t = pt.PrettyTable()
    for i in range(6):
        t.add_column(str(i+1),ticket[i])
    print(t)

def buy_ticket(ticket,row,col):
    if row<1 or row>6 or col<1 or col>5:
        print('输入的行号或列号不正确')
        return
    if ticket[row-1][col-1] == '有票':
        ticket[row-1][col-1] = '已售'
    else:
        print('该座位已售出')
    return ticket
def main():
    ticket = init_table()
    while True:
        show_table(ticket)
        choice = input('请输入要购买的座位行号和列号(如,4,3),按q退出:')
        if choice.lower() == 'q':
            break
        row,col = map(int,choice.split(','))
        buy_ticket(ticket,row,col)

if __name__ == '__main__':
    main()
    
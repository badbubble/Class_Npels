from Class_Npels import Npels
from show_myweb import Show
if __name__ == '__main__':
    username = input('请输入账号(回车后继续):')
    pwd = input('请输入密码(回车后继续):')
    a = Npels(username, pwd)
    s = Show()
    print("#############请选择#################")
    print('1.综合')
    print('2.听说')
    i = input('')
    a.chageBook(i)
    print("####################################")
    print('从第几单元开始？')
    i = input('')
    a.changeUnit(i)
    print("####################################")
    print('输入点击间隔时间(1 -- 60)秒 如果弹出单词框 就把此时间调小一些!')
    i = 10
    a.changeTime(i)
    print('####################################')
    a.ready()
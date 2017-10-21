import time
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from clickList import csslist,clicks,csslist2,clicks2
#倒入模块结束

#建立类
class Npels():
    def __init__(self,username,pwd,timecut = 60,TIME = 10):
        npelsurl = 'http://192.168.100.117/NPELS'  # URL
        self.driver = webdriver.Chrome()  # 使用Chrome浏览器
        self.driver.get(npelsurl)  # 取得driver
       # print(type(self.driver))  为了找bug 查看属性 driver = webdriver.Chrome() self.driver = driver 为空... 抛出异常
        time.sleep(2) #等待页面加载 内网应该比较快
        self.pwd = pwd
        self.username = username
        self.timecut = timecut
        self.TIME = TIME
        self.book = 1 #默认设置为第一本书
        self.unit = 0 #默认设置为全部单元
        self.ccss1 = '#menu-container > ul > li:nth-child(3) > a'
        self.ccss2 = '#menu-container > ul > li:nth-child(1) > a'
        self.css = '#aspnetForm > div.content > div.main_right > div:nth-child(3) > div > div:nth-child(4) > div > ul:nth-child(1) > a'
        self.csslist = csslist.split(',')  #
        self.clicks = clicks.split(',')  # 分离一下
        self.allunits = 8
        self.login()

    def changeTime(self,time): #修改间隔的时间
        self.timecut = time

    def login(self):   #登录
        print('#################################')
        print(self.username)
        print(self.pwd)
        print('#################################')
        self.driver.find_element_by_id("tbName").send_keys(self.username)
        self.driver.find_element_by_id("tbPwd").send_keys(self.pwd)
        self.driver.find_element_by_id('btnLogin').click()
        time.sleep(5) #等待页面加载


    def chageBook(self,num):  #更改默认书籍
        self.book = num

    def changeUnit(self,num): #更改默认单元
        self.unit = num


    def ready(self):
        if self.book == '2':
            self.ccss1 = '.mainmenu > li:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)'
            self.ccss2 = '.mainmenu > li:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)'
            self.css = '#aspnetForm > div.content > div.main_right > div:nth-child(3) > div > div:nth-child(4) > div > ul:nth-child(2) > a'
            self.csslist = csslist2.split(',')
            self.clicks = clicks2.split(',')
            self.allunits = 14
            #print(type(self.unit))
        for i in range( (int(self.unit) - 1),int(self.allunits)):
                self.TIME = 45
                print('此单元将进行%s分钟' % self.TIME)
                self.start(i)

    def start(self,i): #lets go!
        self.driver.switch_to.frame('mainFrame')
        self.driver.find_element_by_css_selector(self.css).click()
        time.sleep(5)
        above = self.driver.find_element_by_css_selector(self.csslist[i])
        time.sleep(3)
        ActionChains(self.driver).move_to_element(above).perform()
        self.driver.find_element_by_css_selector(self.clicks[i]).click()
        time.sleep(8)
        self.driver.switch_to.frame('contentFrame')
        timebefore = time.time()
        while (True):
            self.driver.find_element_by_css_selector(self.ccss1).click()
            time.sleep(int(self.timecut))
            self.driver.find_element_by_css_selector(self.ccss2).click()
            time.sleep(int(self.timecut))
            print('已进行 %s 分钟' % ((time.time() - timebefore) / 60))
            if int(self.TIME) < int((time.time() - timebefore) / 60):
                break
        if self.book == '1' and self.unit == 8:
            self.book = '2'
            self.unit = 1
            self.driver.refresh()
            self.ready()
        self.driver.refresh()

    def __del__(self):
        print("所有内容已经完成，感谢您的使用！")

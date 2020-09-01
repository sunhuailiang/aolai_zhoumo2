import time

import pytest

from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.home_page import HomePage
from page.login_page import LoginPage
from page.me_page import MePage
from page.page import Page

from page.reg_page import RegPage


class TestLogin:

    def setup(self):
        self.driver = init_driver(no_reset=True)
        self.page = Page(self.driver)
        #self.home_page = HomePage(self.driver)
        #self.reg_page = RegPage(self.driver)
        #self.login_page = LoginPage(self.driver)
        #self.me_page = MePage(self.driver)
    def teardown(self):
        time.sleep(3)
        self.driver.quit()
    @pytest.mark.parametrize("args",analyze_data("login_data","test_login"))
    def test_login(self,args):
        self.page.home.login_if_not(self.page.reg(),self.page.login())
    #    username = args["username"]
    #    password = args["password"]
    #    toast = args["toast"]
    #    '''点击关闭更新'''
    #    self.home_page.click_close()
    #    '''点击我的'''
    #    self.home_page.click_me()
    #    '''点击登录账号密码登录'''
    #    self.reg_page.click_login()
    #    '''输入账号'''
    #    self.login_page.input_username(username)
    #    '''输入密码'''
    #    self.login_page.input_paswrod(password)
    #    '''点击登录'''
    #    self.login_page.click_login()


    #获取注册界面属性
    #def test_dome(self):
    #    self.home_page.click_close()
    #    self.home_page.login_if_not()
#

        #if toast is None:
        #    #用用户名的形式断言
        #    assert  self.me_page.get_nikeyname_text() == username
        #    print("已登录")
        #else:
        #    # 用toast参数的形式断言
        #    assert self.login_page.is_toast_exist(toast)
        #    print("未登录")
import time

from base.base_driver import init_driver
from page.home_page import HomePage
from page.login_page import LoginPage
from page.reg_page import RegPage


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.homepage = HomePage(self.driver)
        self.regpage = RegPage(self.driver)
        self.loginpage = LoginPage(self.driver)
    def teardown(self):
        time.sleep(3)
        self.driver.quit()
    def test_login(self):
        '''关闭更新'''
        self.homepage.click_close()
        '''点击我的'''
        self.homepage.click_me()
        '''点击登录账号密码登录'''
        self.regpage.click_login()
        '''输入账号'''
        self.loginpage.input_username("15911104543")
        '''输入密码'''
        self.loginpage.input_paswrod("52111314shl")
        '''点击登录'''
        self.loginpage.click_login()

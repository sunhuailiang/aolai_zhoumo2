import time
from base.base_driver import init_driver
from page.home_page import HomePage
from page.login_page import LoginPage
from page.reg_page import RegPage


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.home_page = HomePage(self.driver)
        self.reg_page = RegPage(self.driver)
        self.login_page = LoginPage(self.driver)
    def teardown(self):
        time.sleep(3)
        self.driver.quit()
    def test_login(self):
        self.home_page.click_close()
        '''点击我的'''
        self.home_page.click_me()
        '''点击登录账号密码登录'''
        self.reg_page.click_login()
        '''输入账号'''
        self.login_page.input_username("15911104543")
        '''输入密码'''
        self.login_page.input_paswrod("52111314shl")
        '''点击登录'''
        self.login_page.click_login()
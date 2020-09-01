from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class RegPage(BaseAction):
    '''已有账号，登录'''
    login_button = By.ID,"com.yunmall.lc:id/textView1"
    '''点击链接 已有账号，登录'''
    def click_login(self):
        self.click(self.login_button)

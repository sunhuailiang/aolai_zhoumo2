from selenium.webdriver.common.by import By
from base.base_action import BaseAction
from page import login_page


class HomePage(BaseAction):
    #更新窗口关闭按钮元素
    close_button = By.ID, "com.yunmall.lc:id/img_close"
    #我的按钮元素
    me_button = By.XPATH, "//*[@resource-id='com.yunmall.lc:id/tab_me' and @text='我']"

    #点击更新窗口关闭按钮
    def click_close(self):
        self.click(self.close_button)
    #点击我的按钮元素
    def click_me(self):
        self.click(self.me_button)

    def login_if_not(self,reg_page,login_page):

        self.click_close()
        self.click_me()

        if self.driver.current_activity == "com.yunmall.ymctoc.ui.activity.MainActivity":
            True
        #点击已有账号密码登录
        reg_page.click_login()
        #输入账号
        login_page.input_username("nihaihaoma")
        #输入密码
        login_page.input_paswrod("52111314shl")
        #点击登录按钮
        login_page.click_login()
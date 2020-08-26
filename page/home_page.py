from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class HomePage(BaseAction):

    close_button = By.ID, "com.yunmall.lc:id/img_close"
    me_button = By.XPATH, "//*[@resource-id='com.yunmall.lc:id/tab_me' and @text='我']"


    def click_close(self):
        self.click(self.close_button)

    def click_me(self):
        self.click(self.me_button)
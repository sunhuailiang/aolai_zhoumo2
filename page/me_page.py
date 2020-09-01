from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class MePage(BaseAction):
    #注册后用户名称
    nikeyname_text_view = By.ID,"com.yunmall.lc:id/tv_user_nikename"
    #获取注册名称
    def get_nikeyname_text(self):
        return self.get_text(self.nikeyname_text_view)
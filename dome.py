from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = dict()
# 需要连接的手机的平台(不限制大小写)
desired_caps['platformName'] = 'Android'
# 需要连接的手机的版本号(比如 5.2.1 的版本可以填写 5.2.1 或 5.2 或 5 ，以此类推)
desired_caps['platformVersion'] = '5.1'
# 需要连接的手机的设备号(andoird平台下，可以随便写，但是不能不写)
desired_caps['deviceName'] = 'huawei p30'
# 需要启动的程序的包名
desired_caps['appPackage'] = 'com.cyanogenmod.filemanager'
# 需要启动的程序的界面名
desired_caps['appActivity'] = '.activities.NavigationActivity'
# 告诉 appium 不要重置应用
desired_caps['noReset'] = True
# 使用 uiautomator2
desired_caps['automationName'] = 'uiautomator2'
#解决中文问题
desired_caps['unicodekeyboard'] = True
desired_caps['resetkeyboard'] = True
# 连接appium服务器
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.press_keycode(4)

def find_toast(driver,message,timeout=3):
    message = "//*[contains(@text,'"+ message+"')]"
    element = WebDriverWait(driver,timeout,0,1).until(lambda x:x.find_element(By.XPATH,message))
    return element.text
print(find_toast(driver,"再次"))
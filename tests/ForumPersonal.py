import time

from selenium.webdriver.common.by import By
from common.Utils import forumDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class ForumPersonal:
    url = ""
    driver = ""
    def __init__(self):
        self.url = "http://127.0.0.1:9580/index.html"
        self.driver = forumDriver.driver
        self.driver.get(self.url)

    def ChangeProfilePhoto(self):
        #修改头像
        self.driver.find_element(By.CSS_SELECTOR, "#index_nav_avatar").click()
        self.driver.find_element(By.CSS_SELECTOR, "#index_user_settings").click()
        self.driver.find_element(By.CSS_SELECTOR,"#settings_input_chooiceAvatar").send_keys(r"C:\Users\tuanzi\Desktop\测试项目\论坛系统\personalfile.jpg")
        forumDriver.getScreeShot()

    def ChangePersonalProfile(self):
        #点进到个人页面清空简介输入框并输入新的新的简介文字
        self.driver.find_element(By.CSS_SELECTOR, "#index_nav_avatar").click()
        self.driver.find_element(By.CSS_SELECTOR, "#index_user_settings").click()
        self.driver.find_element(By.CSS_SELECTOR, "#settings_textarea_remark").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#settings_textarea_remark").send_keys("这是一个自动化测试的个人简介！")
        #滚动页面点击修改按钮
        button = self.driver.find_element(By.CSS_SELECTOR, "#settings_submit_remark")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.driver.execute_script("arguments[0].click()",button)
        #滚动页面到顶部并跳转到个人发帖页面校对个人简介是否修改成功
        self.driver.execute_script("window.scrollTo(0,0);")
        self.driver.find_element(By.CSS_SELECTOR, "#index_nav_avatar").click()
        self.driver.find_element(By.CSS_SELECTOR, "#index_user_profile").click()
        actual = self.driver.find_element(By.CSS_SELECTOR, "#profile_remark").text
        assert actual == "这是一个自动化测试的个人简介！"
        forumDriver.getScreeShot()
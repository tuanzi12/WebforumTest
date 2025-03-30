import time

from selenium.webdriver import ActionChains
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
        wait = WebDriverWait(self.driver, 15)
        self.driver.maximize_window()  # 确保窗口最大化

        # 进入设置页
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#index_nav_avatar"))).click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#index_user_settings"))).click()

        # 输入简介
        remark_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#settings_textarea_remark")))
        remark_input.clear()
        remark_input.send_keys("这是一个自动化测试的个人简介")

        # 定位提交按钮并滚动
        button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#settings_submit_remark")))

        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'nearest'});",
            button
        )
        time.sleep(0.5)  # 等待滚动惯性稳定
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#settings_submit_remark"))).click()

        self.driver.execute_script("window.scrollTo(0,0);")
        time.sleep(0.5)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#index_nav_avatar"))).click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#index_user_profile"))).click()
        time.sleep(0.5)
        actual = self.driver.find_element(By.CSS_SELECTOR, "#profile_remark").text
        assert actual == "这是一个自动化测试的个人简介"
        forumDriver.getScreeShot()
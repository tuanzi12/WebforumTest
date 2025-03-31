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

    def Change_ProfilePhoto(self):
        #修改头像
        #进入个人页面
        self.driver.find_element(By.CSS_SELECTOR, "#index_nav_avatar").click()
        self.driver.find_element(By.CSS_SELECTOR, "#index_user_settings").click()
        self.driver.find_element(By.CSS_SELECTOR,"#settings_input_chooiceAvatar").send_keys(r"C:\Users\tuanzi\Desktop\测试项目\论坛系统\personalfile.jpg")
        forumDriver.getScreeShot()

    def PersonalProfileSucChange(self):
        wait = WebDriverWait(self.driver, 15)
        self.driver.maximize_window()  # 确保窗口最大化

        # 进入个人页面
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#index_nav_avatar"))).click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#index_user_settings"))).click()

        # 定位提交按钮并滚动
        button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#settings_submit_remark")))

        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'nearest'});",
            button
        )
        time.sleep(0.5)  # 等待滚动惯性稳定

        # 输入简介
        remark_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#settings_textarea_remark")))
        remark_input.clear()
        remark_input.send_keys("这是一个自动化测试的个人简介")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#settings_submit_remark"))).click()# 点击修改简介按钮

        # 回到页面顶部并回到发帖页面验证
        self.driver.execute_script("window.scrollTo(0,0);")
        time.sleep(0.5)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#index_nav_avatar"))).click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#index_user_profile"))).click()
        time.sleep(0.5)
        actual = self.driver.find_element(By.CSS_SELECTOR, "#profile_remark").text
        assert actual == "这是一个自动化测试的个人简介"
        forumDriver.getScreeShot()

    def PasswordSucChangeTest(self):
        wait = WebDriverWait(self.driver, 15)
        self.driver.find_element(By.CSS_SELECTOR, "#index_nav_avatar").click()
        self.driver.find_element(By.CSS_SELECTOR, "#index_user_settings").click()
        # 测试场景1：正常修改密码
        # 定位修改按钮并滚动
        button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#settings_submit_password")))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'nearest'});",
            button
        )
        time.sleep(1)  # 等待滚动惯性稳定
        # 修改密码
        self.driver.find_element(By.CSS_SELECTOR, "#settings_input_oldPassword").send_keys("newpsw1")
        self.driver.find_element(By.CSS_SELECTOR, "#settings_input_newPassword").send_keys("newpsw2")
        self.driver.find_element(By.CSS_SELECTOR, "#settings_input_passwordRepeat").send_keys("newpsw2")
        time.sleep(0.5)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#settings_submit_password"))).click()# 点击修改密码按钮
        #重新登录验证
        self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys("TzTest03")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("newpsw2")
        self.driver.find_element(By.CSS_SELECTOR, "#submit").click()
        self.driver.find_element(By.CSS_SELECTOR, "#index_nav_nickname")
        forumDriver.getScreeShot()

    def PasswordFailChangeTest(self):
        wait = WebDriverWait(self.driver, 15)
        self.driver.find_element(By.CSS_SELECTOR, "#index_nav_avatar").click()
        self.driver.find_element(By.CSS_SELECTOR, "#index_user_settings").click()
        # 测试场景2：旧密码错误
        # 2.1 旧密码不匹配
        button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#settings_submit_password")))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'nearest'});",
            button
        )
        time.sleep(1)  # 等待滚动惯性稳定

        self.driver.find_element(By.CSS_SELECTOR, "#settings_input_oldPassword").send_keys("newpswxxx")
        self.driver.find_element(By.CSS_SELECTOR, "#settings_input_newPassword").send_keys("newpsw3")
        self.driver.find_element(By.CSS_SELECTOR, "#settings_input_passwordRepeat").send_keys("newpsw3")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#settings_submit_password"))).click()  # 点击修改密码按钮
        # 出现提示则说明运行失败
        self.driver.find_element(By.CSS_SELECTOR, "body > div.jq-toast-wrap.bottom-right > div")
        forumDriver.getScreeShot()

        # 2.2 新密码与重复不一致

        self.driver.find_element(By.CSS_SELECTOR, "#settings_input_oldPassword").send_keys("newpsw2")
        self.driver.find_element(By.CSS_SELECTOR, "#settings_input_newPassword").send_keys("newpsw")
        self.driver.find_element(By.CSS_SELECTOR, "#settings_input_passwordRepeat").send_keys("newpswxxx")
        #出现提示则说明运行失败
        self.driver.find_element(By.CSS_SELECTOR, "body > div.jq-toast-wrap.bottom-right > div")
        forumDriver.getScreeShot()



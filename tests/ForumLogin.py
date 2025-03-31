
from selenium.webdriver.common.by import By
from common.Utils import forumDriver

class ForumLogin:
    url = ""
    driver = ""
    def __init__(self):
        self.url = "http://127.0.0.1:9580/sign-in.html"
        self.driver = forumDriver.driver
        self.driver.get(self.url)

    def LoginSucTest(self):
        #清空输入框并输入正确的账号密码并点击正常登录
        self.driver.find_element(By.CSS_SELECTOR, "#username").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#password").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys("TzTest03")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("newpsw2")
        self.driver.find_element(By.CSS_SELECTOR, "#submit").click()
        #找到登录后首页的logo即为登陆成功
        self.driver.find_element(By.CSS_SELECTOR, "#index_nav_nickname")
        forumDriver.getScreeShot()


    def LoginFailTest(self):
        self.driver.implicitly_wait(5)
        #输入错误的账号或密码并点击登录
        self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys("TzTest021")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123")
        self.driver.find_element(By.CSS_SELECTOR, "#submit").click()
        #找到错误弹窗确认登录失败
        self.driver.find_element(By.CSS_SELECTOR, "body > div.jq-toast-wrap.bottom-right > div > h2")
        forumDriver.getScreeShot()
        self.driver.back()

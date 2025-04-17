
from selenium.webdriver.common.by import By
from common.Utils import forumDriver


class ForumRegister:
    url = ""
    driver = ""
    def __init__(self):
        self.url = "http://127.0.0.1:9580/sign-up.html"
        self.driver = forumDriver.driver
        self.driver.get(self.url)

    def RegisterSucTest(self):
            #输入新的账号密码并同意协议
            self.driver.find_element(By.CSS_SELECTOR, "#username").clear()
            self.driver.find_element(By.CSS_SELECTOR, "#nickname").clear()
            self.driver.find_element(By.CSS_SELECTOR, "#password").clear()
            self.driver.find_element(By.CSS_SELECTOR, "#passwordRepeat").clear()

            self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys("TzTest1")
            self.driver.find_element(By.CSS_SELECTOR, "#nickname").send_keys("TzTest1")
            self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123")
            self.driver.find_element(By.CSS_SELECTOR, "#passwordRepeat").send_keys("123")
            self.driver.find_element(By.CSS_SELECTOR, "#policy").click()
            self.driver.find_element(By.CSS_SELECTOR, "#submit").click()
            # 能够找到登录界面，说明注册成功，否则注册失败
            self.driver.find_element(By.CSS_SELECTOR, "body > div > div > div > div.col-lg.d-none.d-lg-block > img")
            # 添加屏幕截图
            forumDriver.getScreeShot()

    def RegisterFailTest(self):
        # 输入已存在的用户密码
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys("TzTest03")
        self.driver.find_element(By.CSS_SELECTOR, "#nickname").send_keys("TzTest03")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123")
        self.driver.find_element(By.CSS_SELECTOR, "#passwordRepeat").send_keys("123")
        self.driver.find_element(By.CSS_SELECTOR, "#policy").click()
        self.driver.find_element(By.CSS_SELECTOR, "#submit").click()
        self.driver.find_element(By.CSS_SELECTOR, "body > div.jq-toast-wrap.bottom-right > div > h2")
        forumDriver.getScreeShot()

        # 确认密码与密码不匹配
        self.driver.find_element(By.CSS_SELECTOR, "#passwordRepeat").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#passwordRepeat").send_keys("123123")
        actual = self.driver.find_element(By.CSS_SELECTOR, "#signUpForm > div > div:nth-child(5) > div > div").text
        assert actual == "请检查确认密码"
        # 添加屏幕截图
        forumDriver.getScreeShot()

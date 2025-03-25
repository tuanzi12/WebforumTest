import time

from selenium.webdriver.common.by import By
from common.Utils import forumDriver

class ForumPersonal:
    url = ""
    driver = ""
    def __init__(self):
        self.url = "http://127.0.0.1:9580/index.html"
        self.driver = forumDriver.driver
        self.driver.get(self.url)

    def ChangeProfilePhoto(self):
        self.driver.find_element(By.CSS_SELECTOR, "#index_nav_avatar").click()
        self.driver.find_element(By.CSS_SELECTOR, "#index_user_settings").click()
        self.driver.find_element(By.CSS_SELECTOR, "button.btn[aria-label^='修改头像‘]").click()
        time.sleep(5)
import self as self

import datetime
import os.path
import sys

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class Driver:
    driver = ""

    def __init__(self):
        options = webdriver.EdgeOptions()
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()),options = options)
        self.driver.implicitly_wait(2)

    def getScreeShot(self):
        dirname = datetime.datetime.now().strftime("%Y-%m-%d")
        if not os.path.exists("../images/"+dirname):
            os.mkdir("../images/"+dirname)
        filename = sys._getframe().f_back.f_code.co_name+"-" + datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".png"
        self.driver.save_screenshot("../images/"+dirname+"/"+filename)

forumDriver = Driver()
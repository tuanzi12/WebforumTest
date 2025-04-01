import time
from selenium.webdriver.common.by import By
from common.Utils import forumDriver

class ForumPost:
    url = ""
    driver = ""
    def __init__(self):
        self.url = "http://127.0.0.1:9580/index.html"
        self.driver = forumDriver.driver
        self.driver.get(self.url)


    def PostMessageSucTest(self):
        # 发帖成功
        self.driver.implicitly_wait(5)
        # 点击发布帖子页面
        self.driver.find_element(By.CSS_SELECTOR, "#bit-forum-content > div.page-header.d-print-none > div > div > div.col-auto.ms-auto.d-print-none > div > a.btn.btn-primary.d-none.d-sm-inline-block.article_post").click()
        # 选择分区
        self.driver.find_element(By.CSS_SELECTOR, "#article_post_borad > option:nth-child(2)").click()
        # 输入帖子标题
        self.driver.find_element(By.CSS_SELECTOR, "#article_post_title").send_keys("自动化测试C++")
        # 选择codemirror编辑区
        code_mirror = self.driver.find_element(By.CSS_SELECTOR,"#edit-article > div.CodeMirror.cm-s-default.CodeMirror-wrap.CodeMirror-empty")
        # 输入测试文字
        self.driver.execute_script("arguments[0].CodeMirror.setValue(arguments[1]);",code_mirror,"测试文字")
        # 定位发布按钮
        button = self.driver.find_element(By.CSS_SELECTOR, "#article_post_submit")
        #滚动找到按钮并添加响应时间
        self.driver.execute_script("arguments[0].scrollIntoView()", button)
        time.sleep(0.5)
        button.click()
        #验证是否已发布，如果发布后首页和选择的分区的第一条有显示则证明发布成功
        time.sleep(1)
        text = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div[1]/a/strong").text
        assert text == "自动化测试C++"
        forumDriver.getScreeShot()

    def PostMessageFailTest(self):
        self.driver.implicitly_wait(5)
        # 点击发布帖子页面
        self.driver.find_element(By.CSS_SELECTOR, "#bit-forum-content > div.page-header.d-print-none > div > div > div.col-auto.ms-auto.d-print-none > div > a.btn.btn-primary.d-none.d-sm-inline-block.article_post").click()
        # 选择分区
        self.driver.find_element(By.CSS_SELECTOR, "#article_post_borad > option:nth-child(2)").click()
        # 不输入标题和内容
        button = self.driver.find_element(By.CSS_SELECTOR, "#article_post_submit")

        # 滚动找到按钮并添加响应时间
        self.driver.execute_script("arguments[0].scrollIntoView()", button)
        time.sleep(0.5)
        button.click()

        element = self.driver.find_element(By.XPATH,"/html/body/div[4]/div")
        full_text = element.text
        separator = "\n"  # 或 "\n"、"|" 等实际分隔符
        text_parts = full_text.split(separator)
        third_text = text_parts[2]
        assert third_text == "请输入帖子标题"
        time.sleep(3)
        forumDriver.getScreeShot()

        # 只输入标题不输入内容
            # 输入帖子标题
        self.driver.find_element(By.CSS_SELECTOR, "#article_post_title").send_keys("自动化测试C++")
        self.driver.execute_script("arguments[0].scrollIntoView()", button)
        time.sleep(0.5)
        button.click()

        element = self.driver.find_element(By.XPATH,"/html/body/div[4]/div")
        full_text = element.text
        separator = "\n"  # 或 "\n"、"|" 等实际分隔符
        text_parts = full_text.split(separator)
        third_text = text_parts[2]

        assert third_text == "请输入帖子内容"
        time.sleep(3)
        forumDriver.getScreeShot()

        # 只输入内容不输入标题
            # 清空标题
        self.driver.find_element(By.CSS_SELECTOR, "#article_post_title").clear()
        # 选择codemirror编辑区
        code_mirror = self.driver.find_element(By.CSS_SELECTOR,
                                               "#edit-article > div.CodeMirror.cm-s-default.CodeMirror-wrap.CodeMirror-empty")
        # 输入测试文字
        self.driver.execute_script("arguments[0].CodeMirror.setValue(arguments[1]);", code_mirror, "测试文字")
        self.driver.execute_script("arguments[0].scrollIntoView()", button)
        time.sleep(0.5)
        button.click()

        element = self.driver.find_element(By.XPATH, "/html/body/div[4]/div")
        full_text = element.text
        separator = "\n"  # 或 "\n"、"|" 等实际分隔符
        text_parts = full_text.split(separator)
        third_text = text_parts[2]
        assert third_text == "请输入帖子标题"
        forumDriver.getScreeShot()

    def PostInteraction(self):
        self.driver.find_element(By.CSS_SELECTOR, "#artical-items-body > div:nth-child(1) > div > div.col > div.text-truncate > a").click()
        self.driver.find_element(By.CSS_SELECTOR, "#details_btn_like_count").click()
        time.sleep(0.5)
        vc = self.driver.find_element(By.ID, "details_article_visitCount").text
        lc = self.driver.find_element(By.CSS_SELECTOR, "#details_article_likeCount").text
        assert vc == '1'
        # assert lc == '1'

        # 定位评论区
        code_mirror = self.driver.find_element(By.CSS_SELECTOR,
                                               "#article_details_reply > div.CodeMirror.cm-s-default.CodeMirror-wrap.CodeMirror-empty")

        # 输入测试文字
        self.driver.execute_script("arguments[0].CodeMirror.setValue(arguments[1]);", code_mirror, "评论测试文字")
        # 定位发布按钮
        button = self.driver.find_element(By.CSS_SELECTOR, "#details_btn_article_reply")
        # 滚动找到按钮并添加响应时间
        self.driver.execute_script("arguments[0].scrollIntoView()", button)
        time.sleep(0.5)
        button.click()

        text = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/p").text
        assert text == "评论测试文字"
        forumDriver.getScreeShot()
    def sort(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/header[1]/div/div/div[1]/div/form/div/input").send_keys("自动化测试C++")
        text = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div[1]/a/strong").text
        assert text == "自动化测试C++"
        forumDriver.getScreeShot()
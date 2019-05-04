import os
import time
from selenium import webdriver
from Common.baseui import baseUI


URL = "https://www.damai.cn/"# PC页面


class TestDamai():

    def test_start(self,driver):
        # 打开浏览器
        # 确定chromedriver.exe的位置
        driver_path = os.path.join(os.path.dirname(__file__), "../../chromedriver/chromedriver.exe")
        # 打开浏览器
        driver = webdriver.Chrome(driver_path)
        driver.maximize_window()  # 最大化浏览器
        driver.set_page_load_timeout(15)  # 网页加载超时为10s
        driver.set_script_timeout(10)  # js脚本运行超时10s
        driver.implicitly_wait(10)  # 元素查找超时时间10s

        base = baseUI(driver)

        # 打开网址
        driver.get(URL)









# -*- coding: utf-8 -*-
# @Time    : 2019/5/11 16:21
# @File    : page.py
import win32gui
import win32con
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webdriver import WebElement
from common.my_log import MyLog
from selenium.webdriver import Chrome
from common.project_path import *


class Page:

    def __init__(self, driver: Chrome):
        self.driver = driver
        self.driver.maximize_window()
        self.logging = MyLog()  # 导入日志类

    def find_element_wait(self, locator, timeout=20, poll_frequency=0.5) -> WebElement:
        # 页面元素查找等待
        try:
            wait = WebDriverWait(self.driver, timeout, poll_frequency)
            element = wait.until(ec.presence_of_element_located(locator))
        except Exception as e:
            # 写入日志
            self.logging.error('元素定位失败{}'.format(e))
            self.get_screen_shot('等待元素不可见')
            raise e
        return element

    def click_element_wait(self, locator, timeout=20, poll_frequency=0.5) -> WebElement:

        try:
            # 等待页面元素可以点击
            wait = WebDriverWait(self.driver, timeout, poll_frequency)
            element = wait.until(ec.element_to_be_clickable(locator))
        except Exception as e:
            self.logging.error('元素定位失败{}'.format(e))
            self.get_screen_shot('等待元素不可点击')
            raise e
        return element

    def current_handles(self):
        # 获得当前窗口数
        try:
            handles = self.driver.window_handles
        except Exception as e:
            self.logging.error('获取窗口数失败{}'.format(e))
            raise e
        return handles

    def switch_windows_wait(self, handles, timeout=20, poll_frequency=0.5):
        # 切换新窗口
        try:
            wait = WebDriverWait(self.driver, timeout, poll_frequency)
            wait.until(ec.new_window_is_opened(handles))
            self.driver.switch_to.window(self.driver.window_handles[-1])  # 切换窗口
        except Exception as e:
            self.logging.error('切换窗口失败{}'.format(e))
            raise e

    def switch_frame_wait(self, locator, timeout=20, poll_frequency=0.5) -> WebElement:
        # 切换到frame
        try:
            wait = WebDriverWait(self.driver, timeout, poll_frequency)
            element = wait.until(ec.frame_to_be_available_and_switch_to_it(locator))
            self.driver.switch_to.default_content()
        except Exception as e:
            self.logging.error('frame切换失败{}'.format(e))
            raise e
        return element

    def switch_main_page(self):

        # 切换回主文档,跳出所有frame
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            self.logging.error('回到主界面失败{}'.format(e))
            raise e

    def get_screen_shot(self, name):
        """截图"""
        mkdir(img_path)
        self.driver.save_screenshot(img_path + '//' + name + '.png')

    @staticmethod
    def send_file(file):
        # 上传文件
        time.sleep(2)
        dialog = win32gui.FindWindow("#32770", "打开")  # 一级窗口
        # 找到窗口
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
        edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 四级
        # 操作
        time.sleep(2)
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file)  # 发送文件路径
        time.sleep(2)
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button) # 点击打开按钮




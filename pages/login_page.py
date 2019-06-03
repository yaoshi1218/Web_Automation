# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 17:44
# @File    : login_page.py
from pages.page import Page
from pages.locations.login_location import *
from selenium.webdriver import Chrome


class LoginPage(Page):
    # 登录页面地址
    url = 'http://XXXX/Index/login.html'

    def login(self, username, pwd):
        """登录"""
        self.driver.get(self.url)
        user_ele = self.get_user_info()
        pwd_ele = self.get_pwd_info()
        # 发送用户名密码，
        user_ele.send_keys(username)
        pwd_ele.send_keys(pwd)
        # 点击登录
        self.click_login().click()
        return self.driver

    def get_flash_info(self):
        """获取错误信息"""
        ele = self.find_element_wait(error_location)
        return ele

    def get_authorize_info(self):
        """获得权限提示的文本"""
        ele = self.find_element_wait(authorize_location)
        return ele.text

    def clear_user_info(self):
        """清空用户数据"""
        self.clear_username()
        self.clear_pwd()

    def clear_username(self):
        """清空用户"""
        # 定位用户  get_username()
        return self.get_user_info().clear()

    def clear_pwd(self):
        """清空密码"""
        return self.get_pwd_info().clear()

    def get_user_info(self):
        """定位用户名"""
        ele = self.find_element_wait(user_location)
        return ele

    def get_pwd_info(self):
        """定位密码输入"""
        ele = self.find_element_wait(password_location)
        return ele

    def click_login(self):
        """登录按钮定位"""
        ele = self.click_element_wait(login_button_location)
        return ele


if __name__ == '__main__':
    driver = Chrome()
    LoginPage(driver)

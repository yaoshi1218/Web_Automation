# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 22:58
# @File    : home_page.py
from pages.page import Page
from pages.locations.home_location import *
from selenium.webdriver import Chrome


class HomePage(Page):

    def get_nickname(self):
        """定位昵称"""
        ele = self.find_element_wait(nickname_location)
        return ele

    def click_project(self):
        """点击投标项目"""
        ele = self.click_element_wait(project_name_location)
        return ele.click()




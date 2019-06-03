# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 12:21
# @File    : project_page.py
from pages.page import Page
from pages.locations.project_location import *
from pages.locations.home_location import *


class ProjectPage(Page):
    """投标页面"""

    def investment(self, amount):
        """进行投资"""
        self.get_input_investment().send_keys(amount)

    def get_tender_button(self):
        """定位投标按钮"""
        ele = self.find_element_wait(tender_button_location)
        return ele

    def get_input_investment(self):
        """定位投资输入框"""
        ele = self.find_element_wait(input_investment_location)
        return ele

    def get_balance(self):
        """获取余额"""
        return self.get_input_investment().get_attribute('data-amount')

    def clear_amount_info(self):
        """清空数据"""
        return self.get_input_investment().clear()

    def get_success_info(self):
        """获取成功投资信息"""
        ele = self.find_element_wait(tender_success_location)
        return ele

    def close_success_page(self):
        """关闭投资成功弹窗"""
        ele = self.find_element_wait(close_success_location)
        return ele.click()

    def get_prompt_box(self):
        """定位提示框"""
        ele = self.find_element_wait(prompt_box_location)
        return ele

    def get_confirm_button(self):
        """获取错误弹窗确认按钮"""
        ele = self.click_element_wait(confirm_location)
        return ele

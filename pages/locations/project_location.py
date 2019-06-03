# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 12:05
# @File    : project_location.py

from selenium.webdriver.common.by import By

# 投资输入框
input_investment_location = (By.XPATH, "//input[@data-url='/Invest/invest']")

# 确认投标按钮
tender_button_location = (By.XPATH, "//div[@class='right']//button")

# 投标成功
tender_success_location = (By.XPATH, "//div[@class='layui-layer-content']//div[contains(text(),'投标成功')]")

# 关闭成功界面
close_success_location = (By.XPATH, "//div[@class='layui-layer-content']//div[@class='close_pop']/img")

# 提示框错误信息
prompt_box_location = (By.XPATH, "//div[@class='text-center']")

# 提示框确认按钮
confirm_location = (By.XPATH, "//div[@class='layui-layer-btn']//a")

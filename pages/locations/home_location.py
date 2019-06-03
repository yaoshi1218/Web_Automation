# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 22:59
# @File    : home_location.py
from selenium.webdriver.common.by import By

# 用户昵称
nickname_location = (By.XPATH, "//a [@href='/Member/index.html']")

# 投标的名称
project_name_location = (By.XPATH, "//span[contains(text(),'买老婆')]")

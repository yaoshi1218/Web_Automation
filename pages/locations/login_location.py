# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 17:29
# @File    : login_location.py
from selenium.webdriver.common.by import By


# 手机号输入框
user_location = (By.XPATH, "//input[@name='phone']")

# 密码输入框
password_location = (By.XPATH, "//input[@name='password']")

# 记住账号定位
remember_me_location = (By.XPATH, "//input[@name='remember_me']")

# 登录定位
login_button_location = (By.XPATH, "//button[contains(text(),'登录')]")

# 获取错误信息
error_location = (By.CSS_SELECTOR, '.form-error-info')

# 获取弹窗信息
authorize_location = (By.CLASS_NAME, 'layui-layer-content')

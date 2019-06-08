# -*- coding: utf-8 -*-
# @Time    : 2019/6/8 12:39
# @File    : conftest.py
import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver import Chrome


@pytest.fixture(scope='session')
def web_driver():
    driver = Chrome()
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # driver = webdriver.Chrome(chrome_options=chrome_options)
    yield driver
    driver.quit()


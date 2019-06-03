# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 22:13
# @File    : run.py
import pytest
import os

if __name__ == '__main__':

    pytest.main(["test_case", r"--junitxml=report\test.xml"])
    '''allure serve  allure report'''
    os.system("allure serve  allure report")

# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 18:12
# @File    : test_login.py
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from test_data.login_data import *


@pytest.mark.run(order=1)
@pytest.mark.login
class TestLogin:
    """登录测试类"""

    @pytest.mark.error
    @pytest.mark.parametrize('data', user_info_error)
    def test_login_error(self, data, web_driver):
        """账号密码为空的用例"""
        # 登录
        login_page = LoginPage(web_driver)
        login_page.login(data['username'], data['pwd'])
        # 定位出错的信息的元素 get_flash_info()
        flash_ele = login_page.get_flash_info()
        try:
            # 断言
            assert(data['expected'] == flash_ele.text)
            login_page.logging.info('断言成功')
            login_page.get_screen_shot(data['expected'])
            login_page.logging.info('{}用例成功'.format(data['expected']))
        except AssertionError as e:
            login_page.logging.error('断言出错：'.format(e))
            raise e
        finally:
            # 清空信息
            login_page.clear_user_info()

    @pytest.mark.error
    @pytest.mark.parametrize('data', user_info_authorize)
    def test_login_authorize(self, data, web_driver):
        """手机号没有权限的用例"""
        login_page = LoginPage(web_driver)
        login_page.login(data['username'], data['pwd'])
        try:
            assert (data['expected'] == login_page.get_authorize_info())
            login_page.logging.info('断言成功')
            login_page.get_screen_shot(data['expected'])
            login_page.logging.info('{}：用例成功'.format(data['expected']))
        except AssertionError as e:
            login_page.logging.error('断言出错：'.format(e))
            raise e
        finally:
            # 清空信息
            login_page.clear_user_info()

    @pytest.mark.success
    @pytest.mark.parametrize('data', user_info_success)
    def test_login_success(self, data, web_driver):
        """正确登录的用例"""
        login_page = LoginPage(web_driver)
        login_page.login(data['username'], data['pwd'])
        nickname = HomePage(web_driver).get_nickname().text
        try:
            assert (data['expected'] in nickname)
            login_page.logging.info('断言成功')
            login_page.get_screen_shot(data['expected'])
            login_page.logging.info('{}：用例成功'.format(data['expected']))
        except AssertionError as e:
            self.logging.error('断言出错：'.format(e))
            raise e


if __name__ == '__main__':
    pytest.main()



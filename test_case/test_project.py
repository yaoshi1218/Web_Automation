# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 13:23
# @File    : test_project.py
import pytest,time
from pages.project_page import ProjectPage
from pages.home_page import HomePage
from test_data.investment_data import *


@pytest.mark.investment
class TestInvestment:

    @pytest.fixture(scope='class')
    def click_project(self, web_driver):
        """进入投资项目"""
        HomePage(web_driver).click_project()

    @pytest.mark.error
    @pytest.mark.parametrize('data', error_data)
    def test_investment_error(self, web_driver, click_project, data):
        project_page = ProjectPage(web_driver)
        project_page.investment(data['amount'])
        project_page.get_tender_button().click()
        error_info = project_page.get_prompt_box().text
        try:
            assert (data['expected'] == error_info)
            project_page.logging.info('断言成功')
            project_page.get_screen_shot(data['expected'] + data['id'])  # 保存图片
            project_page.logging.info('{}：用例成功'.format(data['expected']))
        except AssertionError as e:
            project_page.logging.error('断言出错：'.format(e))
            raise e
        finally:
            project_page.get_confirm_button().click()
            project_page.clear_amount_info()

    @pytest.mark.error
    @pytest.mark.parametrize('data', error_rule_data)
    def test_investment_rule(self, web_driver, click_project, data):
        project_page = ProjectPage(web_driver)
        project_page.investment(data['amount'])
        error_info = project_page.get_tender_button().text
        try:
            assert (data['expected'] == error_info)
            project_page.logging.info('断言成功')
            project_page.get_screen_shot(data['expected'] + data['id'])  # 保存图片
            project_page.clear_amount_info()
            project_page.logging.info('{}：用例成功'.format(data['expected']))
        except AssertionError as e:
            project_page.logging.error('断言出错：'.format(e))
            raise e

    @pytest.mark.success
    @pytest.mark.parametrize('data', investment_success_data)
    def test_investment_success(self, web_driver, click_project, data):
        project_page = ProjectPage(web_driver)
        old_balance = float(project_page.get_balance())*100
        project_page.investment(data['amount'])
        project_page.get_tender_button().click()
        success_info = project_page.get_success_info().text
        try:
            assert (data['expected'] in success_info)
            project_page.get_screen_shot(data['expected'] + data['id'])  # 截图
        except AssertionError as e:
            project_page.logging.error('断言出错：'.format(e))
            raise e
        finally:
            project_page.close_success_page()
            web_driver.refresh()
            try:
                new_balance = float(project_page.get_balance())*100
                assert (int(old_balance)-int(data['amount'])*100 == int(new_balance))
                project_page.logging.info('断言成功')
                project_page.logging.info('{}用例成功'.format(data['expected']))
            except AssertionError as e:
                project_page.logging.error('断言出错：'.format(e))
                project_page.logging.info('{}用例失败'.format(data['expected']))


if __name__ == '__main__':
    pytest.main()






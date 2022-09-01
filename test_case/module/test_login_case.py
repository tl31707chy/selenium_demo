# -*- coding: utf-8 -*-
# @Time: 2022/8/23 21:27  
# @Author: TangLei
# @File: test_login_case.py
# Software: PyCharm
import pytest
import os
from page.login_page import LoginPage
import allure
from common.read_data import ReadJson
from common.tool import Tool

tool = Tool()
case_data = ReadJson().get_case_data()


@allure.suite('登录功能')
@allure.feature("登录模块")
# @allure.story('登录模块')
class TestLoginCase:

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('data', case_data['login'])
    def test_login(self, data, is_skip_driver):
        allure.dynamic.title(data['用例标题'])
        allure.dynamic.severity(data['用例等级'])
        self.driver = is_skip_driver(LoginPage, data['用例等级'], data['模块'])
        self.driver.login(tool.get_parameter(data['测试数据']['username']), tool.get_parameter(data['测试数据']['password']))
        if data['标签'] == 'normal_flow':
            result = self.driver.get_home_text()
            assert result == '首页'
        elif data['标签'] == 'error_username_password':
            result = self.driver.get_error_tip()
            assert result == '用户名或者密码错误'

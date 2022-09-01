# -*- coding: utf-8 -*-
# @Time: 2022/8/23 20:44  
# @Author: TangLei
# @File: login_page.py
# Software: PyCharm
from common.base import Base
from common.read_data import ReadYaml
import time

read_yaml = ReadYaml()


class LoginPage(Base):
    element = read_yaml.read_conf('登录页面')

    def input_username(self, username):
        """
        输入用户名
        :param username: 用户名
        :return:
        """
        msg = "输入用户名--{}【{}】".format(username, time.time_ns())
        self.send_keys(self.element['用户名'], username, msg)

    def input_password(self, password):
        """
        输入密码
        :param password: 密码
        :return:
        """
        msg = "输入密码--{}【{}】".format(password, time.time_ns())
        self.send_keys(self.element['密码'], password, msg)

    def login_btn(self):
        """
        点击登录
        :return:
        """
        msg = "点击登录【{}】".format(time.time_ns())
        self.click(self.element['登录'], msg)

    def login(self, username, password):
        """
        登录
        :param username:
        :param password:
        :return:
        """
        self.input_username(username)
        self.input_password(password)
        self.login_btn()

    def get_home_text(self):
        """
        获取首页文本
        :return:
        """
        msg = "获取首页文本【{}】".format(time.time_ns())
        result = self.get_text(self.element['首页'], msg)
        return result

    def get_error_tip(self):
        msg = "获取错误提示文本【{}】".format(time.time_ns())
        result = self.get_text(self.element['错误提示'], msg)
        return result


if __name__ == '__main__':
    test = LoginPage()
    test.open('http://192.168.16.100:81/')
    test.input_username('admin')
    test.input_password('admin')
    test.login_btn()
    time.sleep(2)
    test.quit()

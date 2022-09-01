# -*- coding: utf-8 -*-
# @Time: 2022/8/23 19:16  
# @Author: TangLei
# @File: base.py
# Software: PyCharm
import time
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import project_conf
import allure


class Base:

    def __init__(self, log, url, headless=True, remote=False):
        """
        初始化
        :param log: 日志对象
        :param log: 地址
        :param headless: 是否启用无界面模式，默认不启用
        :param remote: 远程连接地址，默认使用本地
        """
        self.log = log
        # 浏览器启动选项
        options = webdriver.ChromeOptions()
        # 是否启用界面模式
        options.headless = headless
        # 谷歌浏览器跳过【你的连接不是私密连接】
        # options.add_argument('ignore-certificate-errors')
        # 窗口设置为1960,1080
        options.add_argument("--window-size=1960,1080")
        if remote:
            self.driver = webdriver.Remote(command_executor=remote, options=options)
        else:
            self.driver = webdriver.Chrome(options=options)
        # 输入网址, 授权AUTH弹窗登录问题：https: // username: password @ www.baidu.com
        self.driver.get(url)
        self.driver.maximize_window()

    def find_element(self, method_element):
        """
        定位单个元素
        :param method_element: (id,kw)
        :return:
        """
        try:
            ele = WebDriverWait(self.driver, 5, 1).until(EC.presence_of_element_located(method_element))
            return ele
        except NoSuchElementException:
            allure.attach(str(method_element), '未找到元素', attachment_type=allure.attachment_type.TEXT)
            self.log.error('未找到元素：{}'.format(method_element))
        except TimeoutException:
            allure.attach(str(method_element), '定位超时', attachment_type=allure.attachment_type.TEXT)
            self.log.error('定位超时：{}'.format(method_element))
        return None

    def find_elements(self, method_element):
        """
        定位多个元素
        :param method_element: (id,kw)
        :return:
        """
        try:
            ele = WebDriverWait(self.driver, 5, 1).until(EC.presence_of_all_elements_located(method_element))
            return ele
        except NoSuchElementException:
            allure.attach(str(method_element), '未找到元素', attachment_type=allure.attachment_type.TEXT)
            self.log.error('未找到元素：{}'.format(method_element))
        except TimeoutException:
            allure.attach(str(method_element), '定位超时', attachment_type=allure.attachment_type.TEXT)
            self.log.error('定位超时：{}'.format(method_element))
        return None

    def screenshot_png(self, msg):
        """
        截图
        :param msg: 图片名称
        :return:
        """
        self.driver.get_screenshot_as_file(project_conf.img_path + msg + '.png')
        self.allure_attach_png(msg)

    @staticmethod
    def remove_timestamp(msg):
        """
        去除时间戳
        :param msg: 描述
        :return:
        """
        return msg.split('【')[0]

    def send_keys(self, method_element, text, msg):
        """
        输入
        :param method_element: (id,kw)
        :param text: 文本
        :param msg: 截图描述
        :return:
        """
        element = self.find_element(method_element)
        if element:
            element.send_keys(text)
            self.screenshot_png(msg)
            self.log.info("{}".format(self.remove_timestamp(msg)))

    def click(self, method_element, msg):
        """
        点击
        :param method_element: (id,kw)
        :param msg: 截图描述
        :return:
        """
        element = self.find_element(method_element)
        if element:
            element.click()
            self.screenshot_png(msg)
            self.log.info("{}".format(self.remove_timestamp(msg)))

    def get_text(self, method_element, msg):
        """
        获取单个元素文本
        :param method_element: (id,kw)
        :param msg: 截图描述
        :return:
        """
        element = self.find_element(method_element)
        self.screenshot_png(msg)
        if element:
            result = element.text
            self.log.info("{}：{}".format(self.remove_timestamp(msg), result))
            return result

    def refresh(self):
        """
        刷新
        :return:
        """
        self.driver.refresh()

    def quit(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()

    @staticmethod
    def allure_attach_png(msg):
        """
        allure报告里存放截图
        :param msg: 文件名字
        :return:
        """
        allure.attach.file(project_conf.img_path + msg + '.png', msg, attachment_type=allure.attachment_type.PNG)


if __name__ == '__main__':
    test = Base(log=123, url='https://www.cnblogs.com/musen6/p/16555665.html', headless=False)
    test.quit()

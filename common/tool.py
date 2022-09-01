# -*-coding:utf8 -*-
"""
@Time    : 2020/7/6 17:12
@Author  : root
@FileName: tool.py
@CSDN: https://blog.csdn.net/qq_36076898
"""

import random
import string
import re
from faker import Faker


class Tool:

    def __init__(self):
        self.fake = Faker(locale='zh_CN')

    @staticmethod
    def get_random_str(random_length=5):
        """
        生成一个指定长度的随机字符串，其中
        string.digits=0123456789
        string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
        """
        str_list = [random.choice(string.digits + string.ascii_letters) for i in range(random_length)]
        random_str = ''.join(str_list)
        return random_str

    def get_phone_number(self):
        """随机手机号"""
        return self.fake.phone_number()

    def get_email(self):
        """随机邮箱号"""
        return self.fake.ascii_company_email()

    def get_name(self):
        """获取名字"""
        return self.fake.name()

    def get_ipv4(self):
        """获取IP"""
        return self.fake.ipv4()

    @staticmethod
    def get_parameter(data):
        """
        判断某一条数据中是否存在参数，若存在直接替换掉
        :param data:#get_random_str#
        :return:
        """
        p = r"\${(.+?)}"
        try:
            method = re.search(p, data).group(1)
        except:
            method = ''
        if hasattr(Tool, method):
            try:
                test_data = getattr(Tool(), method)()
            except:
                # 静态函数
                test_data = getattr(Tool, method)()
        else:
            test_data = data
        if data:
            result = data.replace('${%s}' % method, test_data)
        else:
            result = ''
        return result


if __name__ == '__main__':
    test = Tool()
    print(test.get_parameter("${get_random_str}"))
    print(test.get_parameter("${get_phone_number}"))
    print(test.get_parameter("${get_name}"))
    print(test.get_parameter("admin"))

# -*-coding:utf8 -*-
"""
@Time    : 2021/8/29 20:33
@Author  : tanglei
@FileName: read_data.py
@CSDN: https://blog.csdn.net/qq_36076898
"""
import json

import yaml
import project_conf


class ReadYaml:
    def __init__(self):
        """
        实例化
        """
        self.file_name = project_conf.element_path
        self.encoding = 'utf-8'

    def read_conf(self, keyword):
        """
        读取yaml文件
        :param keyword: 登录页面
        :return:{'用户名': ['name', 'username'], '密码': ['name', 'password'], '登录': ['xpath', '//*[@id="app"]/div/form/button']}
        """
        # TODO 首先将yaml文件打开，以file对象赋值给conf
        conf = open(file=self.file_name, mode='r', encoding=self.encoding)
        # TODO 然后将这个file对象进行读取
        str_conf = conf.read()
        # TODO 这里使用yaml.Load方法将读取的结果传入进去
        dict_conf = yaml.load(stream=str_conf, Loader=yaml.FullLoader)
        # TODO 取指定的对象，重新凭借数据
        result = {}
        for k, v in dict_conf[keyword].items():
            result[k] = (list(v.keys())[0], list(v.values())[0])
        return result


class ReadJson:

    @staticmethod
    def get_case_data():
        """
        读取用例数据
        :return:
        """
        with open(project_conf.case_path, "r", encoding='utf8') as f:
            case_data = json.load(f)
        return case_data


if __name__ == '__main__':
    res = ReadYaml()
    driver = res.read_conf('登录页面')
    print(driver)

# -*- coding: utf-8 -*-
# @Time: 2022/8/24 13:10  
# @Author: TangLei
# @File: project_conf.py
# Software: PyCharm
import os

# TODO 项目路径
project_path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
# TODO 结果存储路径
result_path = project_path + '/test_result'
# TODO 报告存储路径
report_path = project_path + '/test_result/report'
# TODO 结果json数据存储路径
temp_path = project_path + '/test_result/temp/'
# TODO 截图存储路径
img_path = project_path + '/test_result/img/'
# TODO 元素数据yaml文件位置
element_path = project_path + '/data/elements.yaml'
# TODO 用例数据json文件位置
case_path = project_path + '/data/case_data.json'
# TODO ini文件路径
ini_path = project_path + '/pytest.ini'
# TODO 日志路径
log_path = project_path + '/test_result/log/'


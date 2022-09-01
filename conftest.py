# -*- coding: utf-8 -*-
# @Time: 2022/8/26 18:14  
# @Author: TangLei
# @File: conftest.py
# Software: PyCharm
import loguru
import pytest
import project_conf
from common.read_ini import ReadIni

"""
allure设置用例级别：
blocker： 阻塞缺陷（功能未实现，无法下一步）   
critical：严重缺陷（功能点缺失）             
normal：  一般缺陷（边界情况，格式错误）       
minor：   次要缺陷（界面错误与ui需求不符）     
trivial： 轻微缺陷（必须项无提示，或者提示不规范）
"""
# TODO 创建日志文件
log = loguru.logger
log.add(project_conf.log_path + "/{time}.log", encoding="utf-8", enqueue=True, level='INFO')
read_ini = ReadIni()


def pytest_addoption(parser):
    """
    自定义命令行参数
    :param parser:
    :return:
    """
    parser.addoption("--level", action="store", default="", help="用例等级")
    parser.addoption("--module", action="store", default="", help="功能模块")
    parser.addoption("--headless", action="store", default='1', help="是否启用无界面，默认为0：不启用，启用：1")
    parser.addoption("--host", action="store", default='localhost', help="测试环境")


@pytest.fixture()
def is_skip_driver(request):
    """
    判断是否跳过用例，并启动和打开浏览器
    :return:
    """
    # TODO 获取headless参数
    headless_data = {"0": False, "1": True}
    headless = request.config.getoption("--headless")
    # TODO 获取URL参数
    url = read_ini.get_option('env', request.config.getoption("--host"))

    def _is_skip_driver(instant, level, module):
        global driver
        # TODO 判断是否跳过，根据用例等级、模块进行筛选
        order_level = request.config.getoption("--level")
        order_module = request.config.getoption("--module")
        if order_level == "" and order_module != "":
            if order_module != module:
                pytest.skip("此版本不执行该用例")
        elif order_level != "" and order_module == "":
            if order_level != level:
                pytest.skip("此版本不执行该用例")
        elif order_level != '' and order_module != '':
            if order_level == level and order_module == module:
                pass
            else:
                pytest.skip("此版本不执行该用例")
        # TODO 启动浏览器
        driver = instant(log, url, headless_data[headless])
        return driver

    yield _is_skip_driver
    driver.quit()


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


def pytest_runtest_setup(item):
    """ 在 "pytest_runtest_call(item)" 之前调用 """
    log.info('----------执行用例:{}----------'.format(item.name))


def pytest_runtest_call(item):
    """ 调用并执行测试用例(item) """


def pytest_runtest_teardown(item, nextitem):
    """ 在 "pytest_runtest_call(item)" 之后调用 """
    log.info('----------结束用例:{}----------\n'.format(item.name))
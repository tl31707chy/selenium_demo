# -*- coding: utf-8 -*-
# @Time: 2022/8/23 21:38  
# @Author: TangLei
# @File: main.py
# Software: PyCharm
import os
import pytest
import shutil
from pytest_jsonreport.plugin import JSONReport
from common.send_email import SendMail
import project_conf

send_email = SendMail()


def exists_path():
    """
    判断和创建文件夹
    :return:
    """
    if os.path.exists(project_conf.img_path):
        # TODO 删除文件夹
        shutil.rmtree(project_conf.img_path)

    if os.path.exists(project_conf.temp_path):
        # TODO 删除文件夹
        shutil.rmtree(project_conf.temp_path)

    if os.path.exists(project_conf.log_path) is False:
        os.makedirs(project_conf.log_path)

    # TODO 创建文件夹
    os.makedirs(project_conf.temp_path)
    os.makedirs(project_conf.img_path)


if __name__ == '__main__':
    exists_path()
    plugin = JSONReport()
    pytest.main(['--alluredir', project_conf.temp_path], plugins=[plugin])
    os.system('allure generate {} -o {} --clean'.format(project_conf.temp_path, project_conf.report_path))
    summary = plugin.report.get("summary")
    passed = summary.get("passed", 0)
    failed = summary.get("failed", 0)
    skipped = summary.get("skipped", 0)
    total = summary.get("total", 0)
    total_times = str(plugin.report.get('duration')).split('.')[0]
    success_rate = '%.2f' % (passed / total * 100) + '%'
    send_email.send_html(total, passed, failed, skipped, total_times, success_rate)

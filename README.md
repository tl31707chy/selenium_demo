# UI框架简介

# 介绍

用python+selenium4+pytest+allure完成UI自动化

# 目录

common
       |--base.py（封装selenium基础用法）
       |--read_data.py（封装读取yaml、json文件的方法）
       |--read_ini.py（封装读取ini配置文的件方法）
       |--send_email.py（封装发送邮件的方法）
       |--tool.py（封装生成相关测试数据的方法，如：生成字符串、IP、数字等）

data
    |--case_data.json（存放用例）
    |--elements.yaml（存放元素定位）

page（封装不同页面的方法）

test_case
       |--module（模块用例，如：用户模块）

       |--process（业务流程用例）

conftest.py（pytest的钩子函数）

main.py（执行文件）

project_conf.py（配置项目所有的文件路径）

pytest.ini（pytest的配置文件，以及自己定义的一些数据）

# 使用方法

### 用例格式

```json
{
  "login": [
    {
      "用例编号": "0001",
      "用例标题": "验证登录功能是否正常",
      "标签": "normal_flow",
      "测试数据": {
        "username": "admin",
        "password": "admin"
      },
      "期望结果": "首页",
      "模块": "登录",
      "用例等级": "blocker"
    },
    {
      "用例编号": "0002",
      "用例标题": "验证输入错误的用户是否登录失败",
      "标签": "error_username_password",
      "测试数据": {
        "username": "${get_random_str}",
        "password": "admin"
      },
      "期望结果": "用户名或者密码错误",
      "模块": "登录",
      "用例等级": "normal"
    },
    {
      "用例编号": "0003",
      "用例标题": "验证输入错误的密码是否登录失败",
      "标签": "error_username_password",
      "测试数据": {
        "username": "admin",
        "password": "${get_random_str}"
      },
      "期望结果": "用户名或者密码错误",
      "模块": "登录",
      "用例等级": "normal"
    }
  ]
}
```

### 元素定位格式

```yaml
登录页面:
  用户名:
    name: 'username'
  密码:
    name: 'password'
  登录:
    xpath: '//*[@id="app"]/div/form/button'
  首页:
    xpath: '//span[text()="首页"]'
  错误提示:
    xpath: '//p[text()="用户名或者密码错误"]'
```

### 自定义ini的参数

```markdown
[pytest]
addopts = -vs -n 1 --json-report-file none
testpaths = ./test_case
[email]
mail_host = smtp.163.com
receivers = 1601664015@qq.com,3182668966@qq.com
password = 发送邮箱的校验码
sender = 18782048160@163.com
project_name = 网络仿真系统
task_name = 测试所有主流程
tester = 唐雷
[env]
localhost = http://localhost:81
online = http://101.34.155.179:81
```

### 新增的命令行参数（支持pytest.ini里配置）

`--level`：筛选case_data.json用例等级，默认是全部执行，若传参为blocker，只执行用例等级是blocker的用例，其余用例都会跳过。

`--module`：筛选case_data.json模块，默认是全部执行，若传参为登录，只执行模块是登录的用例，其余用例都会跳过。

`--headless`：是否启用无界面，默认为0：不启用，启用：1

`--host`：支持pytest.ini里env设置的测试环境

### 运行命令

```markdown
python main.py
```
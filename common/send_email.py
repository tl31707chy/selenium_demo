# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.read_ini import ReadIni

read_ini = ReadIni()


class SendMail:
    def __init__(self):
        self.mail_host = read_ini.get_option('email', 'mail_host')
        self.receivers = read_ini.get_option('email', 'receivers').split(',')  # 接受邮箱的人
        self.password = read_ini.get_option('email', 'password')  # 此处未邮箱授权码   为发送人的邮箱授权码
        self.sender = read_ini.get_option('email', 'sender')  # 发送邮箱的人

    def smtp_obj(self, msg):
        """
        邮箱对象
        :param msg: 内容
        :return:
        """
        smtp_obj = smtplib.SMTP()
        smtp_obj.connect(self.mail_host, 25)
        smtp_obj.login(self.sender, self.password)
        smtp_obj.sendmail(self.sender, self.receivers, msg.as_string())
        smtp_obj.close()

    def send_text(self, title, text):
        """
        发送文本
        :param title:标题
        :param text:内容
        :return:
        """
        # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
        msg = MIMEText(text, 'plain', 'utf-8')
        msg['From'] = self.sender
        msg['To'] = ','.join(self.receivers)
        msg['Subject'] = title
        self.smtp_obj(msg)

    def send_html(self, total, passed, skipped, failed, total_times, success_rate):
        """
        发送html页面
        :param total: 用例总数
        :param passed: 通过数
        :param failed: 失败数
        :param skipped: 跳过数
        :param total_times: 总时间
        :param success_rate: 成功率
        :return:
        """
        project_name = read_ini.get_option('email', 'project_name')
        task_name = read_ini.get_option('email', 'task_name')
        tester = read_ini.get_option('email', 'tester')
        text = """
        <body>
          <div style="width: 1920px;height: auto;">
          <div>
           <h2>{}-自动化测试报告</h2>
           <p><span>任务名称：</span><b>{}</b></p>
           <p><span>测试人员：</span><b>{}</b></p>
           <p><span>执行时间：</span><b>{}s</b></p>
           <p><span>用例总数：</span><span><b>{}</b>
             <span>成功数量：</span><b style="color:#00DB00">{}</b>
             <span>失败数量：</span><b style="color:red">{}</b>
             <span>跳过数量：</span><b style="color:#919191">{}</b>
             <span>通过率:</span><b style="color:#00DB00">{}</b></span></p>
           <p>查看详细测试报告，请点击</p>
          </div><a
            target="_blank"
            href="http://10.8.250.71/ui/report";
            style="display:inline-block;margin:0px 0px 5px 5px;padding:6px 8px;font-size:14px;outline:none;
            text-align:center;width: 20%;background: #66B3FF;border-radius: 5px;line-height:30px;
            cursor: pointer;">点击此处下载完整测试报告</a>
          </div>
        </body>
        """.format(project_name, task_name, tester, total_times, total, passed, failed, skipped, success_rate)
        # 邮箱正文内容，第一个参数为内容，第二个参数为格式(html 为网页)，第三个参数为编码
        msg = MIMEText(text, 'html', 'utf-8')
        msg['From'] = self.sender
        msg['To'] = ','.join(self.receivers)
        msg['Subject'] = '【{}】'.format(project_name) + 'UI自动化测试报告'
        self.smtp_obj(msg)

    def send_file(self, title, text, file_path):
        """
        发送附件
        :param title: 标题
        :param text: 内容
        :param file_path:附件
        :return:
        """
        msg = MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = ','.join(self.receivers)
        msg['Subject'] = title
        # 邮箱正文
        msg.attach(MIMEText(text, 'plain', 'utf-8'))
        att = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        # 附件名称非中文时的写法
        # att['Content-Disposition'] = "attachment;filename='{}'".format(send_report_path.split('/')[-1])
        # 附件名称为中文时的写法
        att.add_header("Content-Disposition", "attachment", filename=("gbk", "", file_path.split('/')[-1]))
        msg.attach(att)
        self.smtp_obj(msg)


if __name__ == '__main__':
    sendMail = SendMail()
    # sendMail.send_text('这是一个文本邮箱', '测试一下')
    # sendMail.send_file("这是一个附件邮箱", "请查看附件内容", r'E:\PycharmProjects\selenium4_demo\data\case_data.json')
    sendMail.send_html('这是一个html邮箱')

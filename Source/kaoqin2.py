import sys
import urllib.parse
import urllib.request

from enum import Enum
from PySide2.QtWidgets import (QApplication, QDialog, QLineEdit, QPushButton,
                               QVBoxLayout, QWidget, QLabel, QTextEdit, QLineEdit)


class Form(QWidget):
    class PushType(Enum):
        SYUSYA = 1
        TAISYA = 2

    def __init__(self):
        QWidget.__init__(self)
        # Create widgets
        self.setFixedSize(250, 150)  # 设置窗口固定大小
        self.setWindowTitle("考勤小程序")

        self.userNoLabel = QLabel("工号: ")
        self.userNo = QLineEdit("0CB118023")
        self.pdLabel = QLabel("密码: ")
        self.pd = QLineEdit("Kyqiu123")
        self.pd.setEchoMode(QLineEdit.Password)
        self.syussyabutton = QPushButton("上班")
        self.taisyabutton = QPushButton("下班")

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.userNoLabel)
        layout.addWidget(self.userNo)
        layout.addWidget(self.pdLabel)
        layout.addWidget(self.pd)
        layout.addWidget(self.syussyabutton)
        layout.addWidget(self.taisyabutton)

        # Set dialog layout
        self.setLayout(layout)

        # Add button signal to greetings slot
        self.syussyabutton.clicked.connect(
            lambda: self.Postdata(self.PushType.SYUSYA))
        self.taisyabutton.clicked.connect(
            lambda: self.Postdata(self.PushType.TAISYA))

    def Postdata(self, post_type):
        request_url = 'http://10.110.168.126/cws/srwtimerec'

        request_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cache-Control': 'max-age=0',
            'Content-Length': 56,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'cwsstyle=font_s; JSESSIONID=0000O4-_09IaB5kZCncOT51_ZUS:-1',
            'Host': '10.110.168.126',
            'Origin': 'http://10.110.168.126',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://10.110.168.126/cws/srwtimerec',
            'Upgrade-Insecure-Requests': 1,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36 Edg/79.0.309.71'
        }

        syussya_request_datas = {
            'dakoku': 'syussya',
            # 'user_id': '0CB118023',
            'user_id': self.userNo.text,
            # 'password': 'Kyqiu123',
            'password': self.pd.text,
            'watch': ''
        }

        taisya_request_datas = {
            'dakoku': 'taisya',
            # 'user_id': '0CB118023',
            'user_id': self.userNo.text,
            # 'password': 'Kyqiu123',
            'password': self.pd.text,
            'watch': ''
        }

        if post_type == self.PushType.SYUSYA:
            request_datas = urllib.parse.urlencode(syussya_request_datas)
        elif post_type == self.PushType.TAISYA:
            request_datas = urllib.parse.urlencode(taisya_request_datas)

        request_datas = request_datas.encode('ascii')
        res = urllib.request.Request(
            url=request_url, headers=request_headers, data=request_datas)
        response = urllib.request.urlopen(res)


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())

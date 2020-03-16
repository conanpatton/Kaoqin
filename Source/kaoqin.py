import enum
import json
import sys
import urllib.parse
import urllib.request

from PySide2.QtWidgets import (QApplication, QDialog, QLineEdit, QPushButton,
                               QVBoxLayout, QWidget)


class Type(enum.Enum):
    SYUSSYA = 1
    TAISYA = 2


class Form(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        # Create widgets
        self.syussyabutton = QPushButton("上班")
        self.taisyabutton = QPushButton("下班")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.syussyabutton)
        layout.addWidget(self.taisyabutton)

        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.syussyabutton.clicked.connect(self.PostSyussya)
        self.taisyabutton.clicked.connect(self.PostTaisya)
        self.setWindowTitle("考勤小程序")

    def PostSyussya(self):
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
            'user_id': '0CB118023',
            'password': 'Kyqiu123',
            'watch': ''
        }

        taisya_request_datas = {
            'dakoku': 'taisya',
            'user_id': '0CB118023',
            'password': 'Kyqiu123',
            'watch': ''
        }

        # if post_type == 1:
        #    request_datas = urllib.parse.urlencode(syussya_request_datas)
        # else:
        #    request_datas = urllib.parse.urlencode(taisya_request_datas)
        request_datas = urllib.parse.urlencode(syussya_request_datas)
        request_datas = request_datas.encode('ascii')
        res = urllib.request.Request(
            url=request_url, headers=request_headers, data=request_datas)
        response = urllib.request.urlopen(res)

    def PostTaisya(self):
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
            'user_id': '0CB118023',
            'password': 'Kyqiu123',
            'watch': ''
        }

        taisya_request_datas = {
            'dakoku': 'taisya',
            'user_id': '0CB118023',
            'password': 'Kyqiu123',
            'watch': ''
        }

        # if post_type == 1:
        #    request_datas = urllib.parse.urlencode(syussya_request_datas)
        # else:
        #    request_datas = urllib.parse.urlencode(taisya_request_datas)
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

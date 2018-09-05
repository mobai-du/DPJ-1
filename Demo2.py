# -*- coding: utf-8 -*-

import requests
import json
import time
import re
import xlsxwriter

timeout = 5



class DaibangCrawler(object):
    """
    爬虫类
    """
    client = requests.session()
    LOGIN_URL = 'http://dbzloan.xiaojinqb.cn:8090/sys/login'
    headers = {
        'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}

    LOGIN = False

    def login(self):
        """
        请求登录页面token
        :return:
        """
        try:
            resp = self.client.post(url=self.LOGIN_URL,
                                    data={'username': 'td01', 'password': 'td123', },timeout=(timeout,timeout))    # 这里是用户的账号账号要写在引号里面，密码
            #
            print(resp.text)
            global token
            token = resp.json()['token']
            print(token)
        except Exception as e:
            self.LOGIN_URL = False
            raise
        if resp.status_code != 200:
            self.LOGIN = False
            raise Exception('login error')

        self.LOGIN = True

    def index(self):
        """
        获取数据
        :return:
        """
        time_a = str(time.time() * 10)
        time_a = time_a[:-5]

        if not self.LOGIN:
            self.login()
        data = {
            "applyCode": "",
            "decisionResult": "",
            "idNumber": "",
            "pageNumber": 1,
            "pageSize": 10,    # 这里是请求的用户数量写5个就拿5个用户信息
            "sortOrder": "asc",
            "subCase": "",
            "subChannel": "",
            "userMobile": "",
            "userName": "",
        }

        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "166",
            "Content-Type": "application/json",
            "Host": "dbzloan.xiaojinqb.cn:8090",
            "Origin": "http://dbzloan.xiaojinqb.cn:8090",
            "Referer": "http://dbzloan.xiaojinqb.cn:8090/riskinfo/apply/list_approve.html",
            "token": token,
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }
        resp = self.client.get(url='http://dbzloan.xiaojinqb.cn:8090/risk/apply/listApprove?_'.format(time_a),
                               headers=headers, json=data)
        userinfo = resp.json()['rows']

        rowl = 0
        workbook = xlsxwriter.Workbook('用户信息''.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write(rowl, 0, '姓名')
        worksheet.write(rowl, 1, '电话')
        worksheet.write(rowl, 2, '金额')

        for i in userinfo:
            rowl += 1
            username = i['userName']
            usermobile = i['userMobile']
            applicationAmount = i['applicationAmount']
            worksheet.write(rowl,0,username)
            worksheet.write(rowl,1,usermobile)
            worksheet.write(rowl,2,applicationAmount)

            print('执行写入操作中，写入用户名{},写入电话{},写入金额{}'.format(username,usermobile,applicationAmount))
        workbook.close()


crawler = DaibangCrawler()
crawler.login()
crawler.index()



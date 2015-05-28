#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
>>>GDUT JWXT Login without Verify Code<<<

Author  = Copriwolf
Version = v1.0
Website = http://or2.in
Created on 2015-5-29.

Just for studying Python.
Read more in README.me

'''
import sys
import urllib
import urllib2
import re
import cookielib


reload(sys)
sys.setdefaultencoding('utf-8')


class GDUT:

    def __init__(self):
        self.post_username = '3113008066'
        self.post_password = '**********'

    def login(self):

        view_url = 'http://jwgldx.gdut.edu.cn/default6.aspx'
        view_Request = urllib2.Request(view_url)
        view_Responese = urllib2.urlopen(view_Request)
        view_PageOutput = view_Responese.read().decode('gbk')
        view_Petterm = re.compile(
            '.*?__VIEWSTATE".*?value="(.*?)" />.*?', re.S)
        items = re.findall(view_Petterm, view_PageOutput)

        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        post_url = 'http://jwgldx.gdut.edu.cn/default6.aspx'
        post_data = urllib.urlencode({
            '__VIEWSTATE': items[0],
            'tname': '',
            'tbtns': '',
            'tnameXw': 'yhdl',
            'tbtnsXw': 'yhdl%7Cxwxsdl',
            'txtYhm': self.post_username,
            'txtXm': '',
            'txtMm': self.post_password,
            'rblJs': '%D1%A7%C9%FA',
            'btnDl': '%B5%C7+%C2%BC'})
        post_headers = {
            'Referer': 'http://jwgldx.gdut.edu.cn/default6.aspx',
            'User-Agent': "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        }
        request = urllib2.Request(
            url=post_url,
            data=post_data,
            headers=post_headers)
        result = opener.open(request)

        print result.read().decode('gbk')


sayhi = GDUT()
sayhi.login()

# -*- encoding: UTF-8 -*-
# __author__ = 'lenovo'


import requests

class Requests(object):

    def __init__(self, url):
        self.url = url
        self.result = self.getHTMLText(self.url)

    def getHTMLText(url):
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return "这是个错误"

print(__name__)

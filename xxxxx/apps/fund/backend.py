# coding: utf-8
import datetime
import re
import threading

import requests
from django.core.cache import cache


class FundHelper:

    URL = 'http://fund.eastmoney.com/pingzhongdata/{}.js'

    def __init__(self):
        pass

    @classmethod
    def get_one_data(cls, code):
        if cache.get(code):
            return cache.get(code)
        url = cls.URL.format(code)
        pattern = re.compile(r'var fS_name = "(.*)";var fS_code.*var Data_netWorthTrend = (.*);/\*累计净值走势\*/')

        res = requests.get(url)
        if res.status_code != 200:
            return 0, 0
        name, content = re.findall(pattern, res.text)[0]
        data = eval(content)

        timestamp = [i.get('x') for i in data][-400:]
        y = [i.get('y') for i in data][-400:]
        x = [datetime.datetime.fromtimestamp(i / 1000).strftime('%Y-%m-%d') for i in timestamp]

        cache.set(code, (code, name, x, y))
        return code, name, x, y

    @classmethod
    def get_multiple_data(cls, codes):
        res = []
        thread = []
        for code in codes:
            t = threading.Thread(target=cls.get_one_data ,args=(code,))
            t.start()
            thread.append(t)
        for t in thread:
            t.join()


        return res

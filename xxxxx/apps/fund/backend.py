# coding: utf-8
import datetime
import re
from concurrent.futures import ThreadPoolExecutor

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

        for i in range(3):
            try:
                res = requests.get(url, timeout=5)
                break
            except requests.ReadTimeout:
                pass
        else:
            return code, 0, [0], [1]

        if res.status_code != 200:
            return code, 0, [None], [None]
        name, content = re.findall(pattern, res.text)[0]
        data = eval(content)

        timestamp = [i.get('x') for i in data][-401:]
        y = [i.get('y') for i in data][-401:]
        x = [datetime.datetime.fromtimestamp(i / 1000).strftime('%Y-%m-%d') for i in timestamp]

        cache.set(code, (code, name, x, y), 600)
        return code, name, x, y

    @classmethod
    def get_multiple_data(cls, codes):
        res = []
        executor = ThreadPoolExecutor(max_workers=10)
        for data in executor.map(cls.get_one_data, codes):
            res.append(data)

        return res

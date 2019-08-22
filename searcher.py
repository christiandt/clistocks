import requests
import re


class Searcher:

    def __init__(self, ticker):
        res = requests.get("https://markets.ft.com/data/funds/tearsheet/summary?s={}".format(ticker))
        m = re.search('issueId&quot;:&quot;(.*?)&quot;', res.text)
        self.symbol = m.group(1)

    def __str__(self):
        return self.symbol

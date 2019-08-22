import asciichartpy
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Security:

    def __init__(self, symbol, type='Close'):
        # symbol = issueId on https://markets.ft.com/data/funds/
        # type = Open, Close, High or Low
        self.type = type.capitalize()

        data = {}
        data["days"] = 30
        data["dataNormalized"] = "false"
        data["dataPeriod"] = "Day"
        data["dataInterval"] = 1
        data["endOffsetDays"] = 0
        data["exchangeOffset"] = 0
        data["realtime"] = "false"
        data["yFormat"] = "0.###"
        data["timeServiceFormat"] = "JSON"
        data["rulerIntradayStart"] = 26
        data["rulerIntradayStop"] = 3
        data["rulerInterdayStart"] = 10957
        data["rulerInterdayStop"] = 365
        data["returnDateType"] = "ISO8601"

        elements = {}
        elements["Label"] = "0f8ed383"
        elements["Type"] = "price"
        elements["Symbol"] = symbol
        elements["OverlayIndicators"] = []
        elements["Params"] = {}

        data["elements"] = [elements]

        headers = {'content-type': 'application/json'}

        res = requests.post('https://markets.ft.com/data/chartapi/series', headers=headers, data=json.dumps(data))
        self.api_data = json.loads(res.text)

        self.series = {}
        for range in self.api_data["Elements"][0]["ComponentSeries"]:
            self.series[range["Type"]] = range["Values"]

    def name(self):
        return self.api_data["Elements"][0]["CompanyName"]

    def currency(self):
        return self.api_data["Elements"][0]["Currency"]

    def latest_value(self):
        return round(self.series[self.type][-1], 4)

    def latest_change(self):
        return round(self.series[self.type][-1] - self.series[self.type][-2], 4)

    def latest_change_percentage(self):
        return round((self.series[self.type][-1] - self.series[self.type][-2]) / self.series[self.type][-1] * 100, 2)

    def chart(self, height=10):
        return asciichartpy.plot(self.series[self.type], {"height": height})

    def __str__(self):
        result = "{}\n".format(self.name())
        result += "Current value: {} {}\n".format(str(self.latest_value()), self.currency())
        result += "Latest change: {} ({}%)\n".format(str(self.latest_change()), str(self.latest_change_percentage()))
        result += "{}\n".format(self.chart(height=5))
        return result

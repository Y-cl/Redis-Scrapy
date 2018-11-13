import scrapy
from scrapy.http import  Request
import re
from gupiao.items import GupiaoItem

class AllSpider(scrapy.Spider):
    name = 'all'
    allowed_domains = ['nufm.dfcfw.com']
    start_urls = ["http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=ct&sr=1&ps=50&token=894050c76af8597a853f5b408b759f5d&cmd=C._AB&sty=DCFFITAM&rt=51239127"]
    j = 2
    def parse(self,response):
        data = response.body_as_unicode()
        data = re.findall(r'.*?"(.*?)"',data)
        for i in data:
            a = i.split(',')
            item = GupiaoItem()
            item["type"] = a[0]
            item["daima"] = a[1]
            item["name"] = a[2]
            item["zxj"] = a[3]
            item["jinri"] = a[4], a[5], a[6]
            item["wuri"] = a[7], a[8], a[9]
            item["shiri"] = a[10], a[11], a[12]
            item["bankuai"] = a[-3]
            item["time"] = a[-1]

            if a[1][0:3] == '200':
                item['gushi'] = '深市B股'
            elif a[1][0:3] == '900':
                item['gushi'] = '沪市B股'
            elif a[1][0:3] == '002':
                item['gushi'] = '中小板'
            elif a[1][0:3] == '300':
                item['gushi'] = '创业板'
            elif a[1][0:3] == '000' or a[1][0:3] == '001':
                item['gushi'] = '深市A股'
            else:
                item['gushi'] = '沪市A股'

            if a[6] == '-':
                a[6] = 0
                if float(a[6]) >= 10:
                    item['zd'] = '涨停'
                elif float(a[6]) > 0 and float(i.split(',')[1][0:3]) < 10:
                    item['zd'] = '上涨'
                elif float(a[6]) < 0 and float(i.split(',')[1][0:3]) > -10:
                    item['zd'] = '下跌'
                elif float(a[6]) <= -10:
                    item['zd'] = '跌停'
                else:
                    item['zd'] = '持平'
            yield item

    #     if self.j <= int(page):
    #         url = "http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=ct&st=(FFRank)&sr=1&p=%s&ps=50&js={pages:(pc),data:[(x)]}&token=894050c76af8597a853f5b408b759f5d&cmd=C._AB&sty=DCFFITAM&rt=51239127" % self.j
    #         yield self.next_request(url)
    #
    #     self.j += 1
    #
    # def next_request(self, url):
    #     """
    #     做分页请求
    #     :param url:
    #     :return:
    #     """
    #     return Request(url)



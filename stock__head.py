
import scrapy
import json
import re
from gupiao.items import KuozhanItem
from gupiao.items import Kuozhan_xianItem

class KuozhanSpider(scrapy.Spider):
    name = 'kuozhan'
    allowed_domains = ['nuff.eastmoney.com','pdfm.eastmoney.com','pdfm2.eastmoney.com']
    start_urls = ['http://nuff.eastmoney.com/EM_Finance2015TradeInterface/JS.ashx?id=0000011','http://pdfm2.eastmoney.com/EM_UBG_PDTI_Fast/api/js?id=0000011&TYPE=t5&isCR=false']

    def parse(self, response):
        data = response.body_as_unicode()
        data = re.findall('.*?"(.*?)"', data)
        if "pdfm" in response.url:
            data = response.text
            data = data.replace('\r', '')[1:-1].split('\n')
            item = Kuozhan_xianItem()
            item['info'] = data
            yield item
        else:
            item = KuozhanItem()
            item["n"] = data[27]
            item["jinkai"] = data[30]
            item["zuoshou"] = data[36]
            item["zuigao"] = data[32]
            item["zuidi"] = data[34]
            item["fu"] = data[31]
            item["e"] = data[29]
            item["huanshou"] = data[39]
            item["zhenfu"] = data[52]
            item["cjl"] = data[33]
            item["cje"] = data[37]
            yield item


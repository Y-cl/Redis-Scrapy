# # -*- coding: utf-8 -*-
# import re
# import scrapy
# from gupiao.items import PanItem
# import redis
# import json
# from scrapy.http import Request
#
# class PanSpider(scrapy.Spider):
#     name = 'pan'
#     allowed_domains = ['pdfm2.eastmoney.com']
#
#     pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
#     r = redis.StrictRedis(connection_pool=pool)
#     data = r.lrange('all:items', 0, -1)
#     l = []
#     for i in range(len(data)):
#         a = json.loads(data[i])
#         if (a["daima"]+ a["type"]) not in l:
#             l.append(a["daima"]+a["type"])
#
#     start_urls = ["http://pdfm2.eastmoney.com/EM_UBG_PDTI_Fast/api/js?id={}&TYPE=K&js=(x)&rtntype=5&style=top&num=120".format(l[0])]
#
#     n = 1
#     def parse(self, response):
#         data = response.body_as_unicode()
#         data = json.loads(data)
#         l = []  #数据的列表
#         for i in data["data"][-60:-1]:
#             i = i.split(',')
#             a = i[3]
#             i[3] = i[4]
#             i[4] = a
#             l.append(i)
#         print(l)
#         dm = self.l[self.n-1][0:-1]  #daima
#         d = {dm:l}
#
#         item = PanItem()
#         item["d"] = d
#         yield item
#         # for i in d["data"]:
#         #     d = i.split(",")
#         #     print(d[1])
#         #     print(d[2])
#         #     print(d[3])
#         #     print(d[4])
#         #     print("*"*10)
#         # for i in range(1,5):
#         #     print(d["data"][i])
#         # pattern = re.compile('.*?name":"(.*?)",.*?code":"(.*?)",.*?info":(.*?) ')
#         # for item in re.findall(d,pattern):
#         #     qq['name'] = item[0]
#         #     qq['code'] = item[1]
#
#
#         if self.n < len(self.l):
#             url = "http://pdfm2.eastmoney.com/EM_UBG_PDTI_Fast/api/js?id={}&TYPE=K&js=(x)&rtntype=5&style=top&num=120".format(self.l[self.n])
#             yield self.next_request(url)
#         self.n +=1
#
#     def next_request(self, url):
#         return Request(url)
#
#
#
#

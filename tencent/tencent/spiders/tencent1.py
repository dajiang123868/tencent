# -*- coding: utf-8 -*-
import scrapy

from tencent.items import TencentItem


class Tencent1Spider(scrapy.Spider):
    name = 'tencent1'
    allowed_domains = ['tencent.com']
    # 修改起始url
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        # 获取节点的列表
        node_list = response.xpath("//tr[@class='even']|//tr[@class='odd']")
        for node in node_list:
            item = TencentItem()
            item['name'] = node.xpath('./td[1]/a/text()').extract()[0]
            item['detail_link'] = 'https://hr.tencent.com/' + node.xpath('./td[1]/a/@href').extract()[0]
            # extract_first()提取结果的第一个，如果存在则提取，如果不存在则赋值为None
            item['category'] = node.xpath('./td[2]/text()').extract_first()
            item['number'] = node.xpath('./td[3]/text()').extract()[0]
            item['address'] = node.xpath('./td[4]/text()').extract()[0]
            item['pub_date'] = node.xpath('./td[5]/text()').extract()[0]

            # 返回数据给引擎
            yield item
            next_url = 'https://hr.tencent.com/' + response.xpath('//*[@id="next"]/@href').extract()[0]
            # 判断是否到达最后一页
            if 'javascript:;' not in next_url:
                # 没有到达最后一页就发送请求，模拟翻页
                yield scrapy.Request(next_url, callback=self.parse)
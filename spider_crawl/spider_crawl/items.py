# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import response
import scrapy


class SpiderCrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    item["title"] = response.xpath(
            '//*[@id="itemcase_basic"]/div[1]/h1/text()'
        ).extract_first()

    item["s_price"] = response.xpath(
            '//*[@id="itemcase_basic"]/div[1]/p/span/strong/text()'
        ).extract_first().replace(",", "")

    try:
        item["o_price"] = response.xpath(
                '//*[@id="itemcase_basic"]/div[1]/p/span/span/text()'
            ).extract_first().replace(",", "")

    except:
        item["o_price"] = item["s_price"]

    item["discount_rate"] = str(round((1 - int(item["s_price"]) / int(item["o_price"]))*100, 2)) + "%"
    item["link"] = response.url  # 요청한 링크 얻기

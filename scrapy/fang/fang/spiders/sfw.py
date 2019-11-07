# -*- coding: utf-8 -*-
import scrapy
import re
from fang.items import NewHouseItem, ESFHouseItem
from scrapy_redis.spiders import RedisSpider


class SfwSpider(RedisSpider):
    name = 'sfw'
    allowed_domains = ['fang.com']
    # start_urls = ['https://www.fang.com/SoufunFamily.htm']
    handle_httpstatus_list = [301, 302]
    redis_key = "fang:start_urls"

    def parse(self, response):
        trs = response.xpath("//div[@class='outCont']//tr")
        province = None
        for tr in trs:
            tds = tr.xpath("./td[not(@class)]")
            province_text = tds[0].xpath(".//text()").get()
            province_text = re.sub(r"\s", "", province_text)
            if province_text:
                province = province_text
            if province == '其它':
                continue
            city_links = tds[1].xpath(".//a")
            for city_link in city_links:
                city = city_link.xpath(".//text()").get()
                city_url = city_link.xpath(".//@href").get()
                # 构建新房url
                url_module = city_url.split('.')
                scheme = url_module[0]
                domain = "".join("." + url_module[1] + "." + url_module[2])
                newhouse_url = scheme + ".newhouse" + domain + "house/s/"
                # 构建二手房url
                esf_url = scheme + ".esf" + domain
                # if city == '北京':
                #     newhouse_url = 'https://newhouse.fang.com/house/s/'
                #     esf_url = 'https://esf.fang.com/'

                # yield scrapy.Request(url=newhouse_url, callback=self.parse_newhouse, meta={"info": (province, city)})
                yield scrapy.Request(url=esf_url, callback=self.parse_esf, meta={"info": (province, city)})
                break
            break

    def parse_newhouse(self, response):
        province, city = response.meta.get('info')
        lis = response.xpath("//div[contains(@class,'nl_con')]/ul/li")
        for li in lis:
            if li.xpath(".//div[@class='nlcd_name']/a/text()").get() == None:
                continue
            name = li.xpath(".//div[@class='nlcd_name']/a/text()").get().strip()
            house_type_list = li.xpath(".//div[contains(@class,'house_type')]/a/text()").getall()
            house_type_list = list(map(lambda x: re.sub(r"\s", "", x), house_type_list))
            rooms = list(filter(lambda x: x.endswith("居") or x.endswith("上"), house_type_list))
            area = "".join(li.xpath(".//div[contains(@class,'house_type')]/text()").getall())
            area = re.sub(r"\s|－|/", "", area)
            address = li.xpath(".//div[@class='address']/a/@title").get()
            district_text = "".join(li.xpath(".//div[@class='address']/a//text()").getall())
            district = re.search(r".*\[(.+)\].*", district_text).group(1)
            sale = li.xpath(".//div[contains(@class,'fangyuan')]/span/text()").get()
            price = "".join(li.xpath(".//div[@class='nhouse_price']//text()").getall())
            price = re.sub(r"\s|广告", "", price)
            origin_url = li.xpath(".//div[@class='nlcd_name']/a/@href").get()
            origin_url = response.urljoin(origin_url)
            # print(name)
            # print(rooms)
            # print(area)
            # print(address)
            # print(district)
            # print(sale)
            # print(price)
            # print(origin_url)
            # print('=' * 20)
            item = NewHouseItem(
                province=province,
                city=city,
                name=name,
                price=price,
                rooms=rooms,
                area=area,
                address=address,
                district=district,
                sale=sale,
                origin_url=origin_url
            )
            yield item

        next_url = response.xpath("//div[@class='page']//a[@class='next']/@href").get().strip()
        next_text = response.xpath("//div[@class='page']//a[@class='next']/text()").get().strip()
        if next_url and "下一页" in next_text:
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_newhouse,
                                 meta={"info": (province, city)})

    def parse_esf(self, response):
        province, city = response.meta.get('info')
        dls = response.xpath("//div[contains(@class,'shop_list')]/dl")
        for dl in dls:
            if dl.xpath(".//p[@class='add_shop']/a/text()").get() == None:
                continue
            name = dl.xpath(".//p[@class='add_shop']/a/text()").get().strip()
            infos = dl.xpath(".//p[@class='tel_shop']/text()").getall()
            infos = list(map(lambda x: re.sub(r"\s", "", x), infos))
            rooms = ''
            floor = ''
            toward = ''
            year = ''
            area = ''
            for info in infos:
                if "厅" in info or "拼" in info or "栋" in info or "排" in info:
                    rooms = info
                elif "层" in info:
                    floor = info
                elif "向" in info:
                    toward = info
                elif "年" in info:
                    year = info.replace("年建", "")
                elif "㎡" in info:
                    area = info
            address = dl.xpath(".//p[@class='add_shop']/span/text()").get().strip()
            price = "".join(dl.xpath(".//dd[@class='price_right']/span[1]//text()").getall()).strip()
            unit = "".join(dl.xpath(".//dd[@class='price_right']/span[2]//text()").get().strip())
            detail_url = dl.xpath(".//h4/a/@href").get()
            origin_url = response.urljoin(detail_url)

            item = ESFHouseItem(
                province=province,
                city=city,
                name=name,
                rooms=rooms,
                floor=floor,
                toward=toward,
                year=year,
                address=address,
                area=area,
                price=price,
                unit=unit,
                origin_url=origin_url
            )
            yield item

        next_url = response.xpath("//div[@class='page_al']/p[last()-2]/a/@href").get().strip()
        next_text = response.xpath("//div[@class='page_al']/p[last()-2]/a/text()").get().strip()
        if next_url and "下一页" in next_text:
            yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse_esf,
                                 meta={"info": (province, city)})

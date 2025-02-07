import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TraveldodmilSpider(CrawlSpider):
    name = "travelDodMil"
    allowed_domains = ["travel.dod.mil"]
    start_urls = ["https://www.travel.dod.mil/"]

    rules = (Rule(LinkExtractor(allow = (), deny = ["calendar", "location-contact","DTMO-Site-Map/FileId/"],unique = True), callback="parse_item", follow=True),)

    def parse_item(self, response):
        yield {
            "Link": response.url
        }

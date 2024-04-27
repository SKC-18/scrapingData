import scrapy


class DarazspiderSpider(scrapy.Spider):
    name = "darazspider"
    allowed_domains = ["www.daraz.com.np"]
    start_urls = ["https://www.daraz.com.np/catalog/?q=Apple++watch+"]

    def parse(self, response):
        pass

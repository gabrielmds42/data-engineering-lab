import scrapy


class NintendoSpider(scrapy.Spider):
    name = "nintendo"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/nintendo-3ds"]

    def parse(self, response):
        
        products = response.css("div.ui-search-result__wrapper")

        for product in products:
            yield {
                'brand': product.css('span.poly-component__brand::text').get(),
                'name': product.css('a.poly-component__title::text').get(),
            }
        

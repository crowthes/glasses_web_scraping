import scrapy

class GlassesScraper(scrapy.Spider):
    name = 'glasses'
    # I have deleted out the name of the website
    start_urls = ['+str(x)+'' for x in range(1,15)]

    def parse(self,response):
        for products in response.css('div.color-swatch.clearfix'):
            yield{
                'id':products.css('a::attr(data-sku-id)').get(),
                'name':products.css('a::attr(aria-label)').get(),       
                'price':products.css('a::attr(data-list-price)').get(),
                'in_stock':products.css('a::attr(data-instock)').get(),
                'link':products.css('a::attr(data-url)').get()
            }
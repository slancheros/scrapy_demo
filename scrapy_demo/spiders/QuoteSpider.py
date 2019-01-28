import scrapy

class QuoteSpider(scrapy.Spider):
    name="quotes"


    def start_requests(self):
        urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
        ]

        def parse(self, response):
            page = response.url.split("/")[-2]
            filename = 'quotes-%s.html' % page
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)
            print(self.log)

import scrapy



class PriceSpiderSpider(scrapy.Spider):
    name = 'price_spider'

    # setting header for our scraper
    headers = {'referer': 'http://www.google.com',
               'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"
               }

    def start_request(self,url):
        start_urls = ["https://www.amazon.in/LetsShave-Lithium-ion-Cordless-Stainless-settings/dp/B084JPN4M9/ref=sr_1_59_sspa?dchild=1&keywords=Philips&qid=1600875719&sr=8-59-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEySEtOWE4zTjhXWllVJmVuY3J5cHRlZElkPUEwMjk3Mzk0MlZFU1NIUFRXS0c3VCZlbmNyeXB0ZWRBZElkPUEwMTQxMjI5Mk42SlFRV0lFMUdDQyZ3aWRnZXROYW1lPXNwX2J0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=&tag=revmeup-21"]
        
        
        for url in start_urls:
            a = scrapy.Request(url=url, callback=self.amazon_parser, headers=self.headers)
            return(a)
   
    def amazon_parser(self, response):
        
        DEFAULT_REQUEST_HEADERS = {
                'referer': 'http://www.google.com',
                'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"
            }
        product_price = response.css('#priceblock_saleprice::text').extract()
        return(product_price)
        print(product_price)
        
        

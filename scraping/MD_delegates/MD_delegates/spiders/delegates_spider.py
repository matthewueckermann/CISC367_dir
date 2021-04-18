import scrapy
import re

class DelegatesSpider(scrapy.Spider):
    name = "delegates"

    start_urls = [
        'https://msa.maryland.gov/msa/mdmanual/06hse/html/hseal.html'
    ]

    def parse(self,response):
        for del_url in response.css('li a::attr(href)').getall():
            new_url = response.urljoin(del_url)
            yield scrapy.Request(new_url, callback=self.parseDelegates)
        
    
    def parseDelegates(self, response):
        yield {
            'Name' : response.css('b').re(r'\w+ \w*\.? ?\(?\w*\)? ?\w+ ?\w* ?\,? ?\w*\.?')[0],  #\w+\s?\w*\.?\s?\(?\w+?\)?\s\w+\s?\w*
            'Party' : response.css('i').re(r'Democrat|Republican')[0],
            'District': response.css('i').re(r'District \w+')[0],
            'County' : response.css('a::text').getall()[1],
            'Phone' : response.css('ul').re(r'\(\d\d\d\) \d\d\d-\d\d\d\d')[0], # takes the first number
            'Email' : response.css('ul').re(r'\w+\.\w+@house\.state\.md\.us')[0]
        }
        

import scrapy
from scrapy_playwright.page import PageMethod


class TamilDropsSpider(scrapy.Spider):
    name = 'TamilDropsLinks'
    # start_urls = ['https://vaiyan.blogspot.com/p/p.html']

    def start_requests(self):
        start_url = getattr(self, "start_url", None)
        if start_url is None:
            return

        yield scrapy.Request(start_url, meta={
            "playwright": True,
            # page takes longer to render content so - wait for 5 seconds
            'playwright_page_methods': [PageMethod('wait_for_timeout', 5000)]
        })

    def parse(self, response, **kwargs):
        links = response.css('body > div.viewitem-panel > div > div.viewitem-inner > div > div > div.article-content.entry-content a::attr(href)').getall()

        # de-dupe
        links = set(links)

        # only get relevant links
        links = [x for x in links
                     if x.startswith('https://vaiyan.blogspot.com/20')
                     or x.startswith('http://vaiyan.blogspot.com/20')
                     and x.endswith('.html')]
        links.sort()

        yield {'links': links}

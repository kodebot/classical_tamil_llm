import json

import scrapy
from scrapy_playwright.page import PageMethod


class TamilDropsSpider(scrapy.Spider):
    name = 'TamilDropsText'

    # start_urls = ['https://vaiyan.blogspot.com/p/p.html']

    def start_requests(self):
        links_file = getattr(self, "links_file", None)
        if links_file is None:
            return

        links_json = json.load(open(links_file))
        for link in links_json[0]['links']:
            yield scrapy.Request(link, meta={
                "playwright": True,
                # page takes longer to render content so - wait for 5 seconds
                'playwright_page_methods': [PageMethod('wait_for_timeout', 5000)]
            })

    def parse(self, response, **kwargs):
        title = ''.join(response.css(
            'body > div.viewitem-panel > div > div.viewitem-inner > div > div > div.article-header > h1 > a ::text').extract()).strip()
        content = response.css(
            'body > div.viewitem-panel > div > div.viewitem-inner > div > div > div.article-content.entry-content > div ::text').extract()

        yield {
            "title": title,
            "content": content
        }

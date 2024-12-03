# Tamildrops Spiders

## How to run?

First run `tamildrops_links_spider` by passing in index page a as `start_url`

```bash
scrapy runspider tamildrops_links_spider.py -a start_url=https://vaiyan.blogspot.com/p/p.html -O puranaanuru_links.json
```

Then run `tamildrops_text_spider.py`

```bash
scrapy runspider tamildrops_text_spider.py -a links_file=puranaanuru_links.json -O puranaanuru_text.json
```
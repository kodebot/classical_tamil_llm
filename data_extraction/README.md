# Data Extraction

## Setup

Install scrapy in an isolated environment using conda

```shell
conda create --name scraping
conda activate scraping

conda install -c conda-forge scrapy
```

Create new Spider

```shell
scrapy startproject <projectname>
```

example
```shell
scrapy startproject tamildrops
```

Configure Playwright for scraping

Playwright is useful to load pages that gets loaded dynamically using some JS framework

```shell
pip install scrapy-playwright
```

run the following to install headless browsers for playwright

```shell
playwright intstall # for all browsers
playwright install chrome # just for chrome
```

Then replace the DOWNLOAD_HANDLERS in `settings.py` with the following
```
# settings.py
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}
```

## Scrapy Shell

### 1. How to run shell with playwright

1. Make sure you are inside the scrapy project folder that is configured to use playwright, for example `tamildrops`
2. run `scrapy shell`
3. within the shell import PageMethod then issue fetch command with playwright settings 

```python
from scrapy_playwright.page import PageMethod
fetch('https://vaiyan.blogspot.com/p/p.html', meta={'playwright': True, 'playwright_page_methods':[PageMethod('wait_for_timeout', 5000)]})
```
### 2. Useful Shell tips and Selectors

1. Use `view(response)` to view the entire response as html page in browser

2. Get all the text from the page - `''.join(response.xpath("//html//text()").extract()).strip()`

3. Get text/href and nested text/href

```
response.css('body *::text') # get all the text from body and all the elements nested in body
response.css('body::text') # get text only from body
response.css('body ::text') # get text only from body and its child

```

## Run Spider

navigate to the spiders folder and run 
`scrapy runspider tamil_drops_spider.py -O puranaanuru-links.jsonl`


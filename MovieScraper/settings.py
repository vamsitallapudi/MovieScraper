# Scrapy settings for MovieScraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "MovieScraper"

SPIDER_MODULES = ["MovieScraper.spiders"]
NEWSPIDER_MODULE = "MovieScraper.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "MovieScraper (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "MovieScraper.middlewares.MoviescraperSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'MovieScraper.middlewares.MoviescraperDownloaderMiddleware': 543,
    # 'MovieScraper.middlewares.ScrapeOpsFakeUserAgentMiddleware': 400,
    # 'MovieScraper.middlewares.ScrapeOpsFakeBrowserHeaderAgentMiddleware': 400,
    # 'MovieScraper.middlewares.ScrapeOpsProxyMiddleware': 725,
    # "scrapy_cloudflare_middleware.middlewares.CloudFlareMiddleware": 560,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "MovieScraper.pipelines.MoviescraperPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

USER_AGENTS = [
    (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'),
    # ('Mozilla/5.0 (X11; Linux x86_64) '
    #  'AppleWebKit/537.36 (KHTML, like Gecko) '
    #  'Chrome/57.0.2987.110 '
    #  'Safari/537.36'),  # chrome
    # ('Mozilla/5.0 (X11; Linux x86_64) '
    #  'AppleWebKit/537.36 (KHTML, like Gecko) '
    #  'Chrome/61.0.3163.79 '
    #  'Safari/537.36'),  # chrome
    # ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) '
    #  'Gecko/20100101 '
    #  'Firefox/55.0')  # firefox
]

# SCRAPEOPS_API_KEY = '8fd7fdd3-9d94-4177-a795-4049f768dcc1'
# SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT = 'https://headers.scrapeops.io/v1/user-agents'
# SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True
# SCRAPEOPS_NUM_RESULTS = 5
# SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED = True
# SCRAPEOPS_PROXY_ENABLED = True

# CUSTOM_HEADERS = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
#     'Cache-Control': 'no-cache',
#     # 'Cookie': '_cfuvid=FMcy5rSmaph9JZTg7uCPskeGN_Zg7WvtofTrtEKBQD4-1702185861886-0-604800000; WZRK_G=c9a3b7fe33ab4259984502ba58098919; _gcl_au=1.1.340894221.1702185863; _ga=GA1.1.1013980103.1702185864; __cfruid=03b3ed899125c03faad6b7a486396ee8626d4a9b-1702185864; tvc_bmscookie=GA1.2.1013980103.1702185864; tvc_bmscookie_gid=GA1.2.759822804.1702185866; rgn=%7B%22Lat%22%3A%2217.385044%22%2C%22Seq%22%3A%224.0%22%2C%22Long%22%3A%2278.486671%22%2C%22regionName%22%3A%22Hyderabad%22%2C%22regionCode%22%3A%22HYD%22%2C%22isOlaEnabled%22%3A%22N%22%2C%22regionCodeSlug%22%3A%22hyd%22%2C%22regionNameSlug%22%3A%22hyderabad%22%2C%22GeoHash%22%3A%22tep%22%7D; G_ENABLED_IDPS=google; bmsId=1.774277133.1702185933098; preferences=%7B%22ticketType%22%3A%22M-TICKET%22%7D; cf_clearance=d2omcOlELor5R.GDI3iGJH3frLaHIYSJty6i0I1d.cM-1702198216-0-1-e2ec13c5.f0e21527.a77b70ef-0.2.1702198216; AMP_TOKEN=%24NOT_FOUND; __cf_bm=A5UlVsRvuDyxqtGdJbjXp3iojtYugrFE3G9GqwTvCkg-1702204337-1-AUeeBtWvAiheGlGhojXTYfb0P7bYqq9WLWjVY3II349BvhVa7pxBagKCIgfFIhZ4k/tf+YtL/Sqeck6P1HEcSeY=; WZRK_S_RK4-47R-98KZ=%7B%22p%22%3A3%2C%22s%22%3A1702203085%2C%22t%22%3A1702204364%7D; _ga_84T5GTD0PC=GS1.1.1702200148.4.1.1702204387.11.0.0',
#     'Pragma': 'no-cache',
#     'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
#     'Sec-Ch-Ua-Mobile': '?0',
#     'Sec-Ch-Ua-Platform': '"macOS"',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-User': '?1',
#     'Service-Worker-Navigation-Preload': 'true',
#     'Upgrade-Insecure-Requests': '1',
# }

CUSTOM_HEADERS = {
    'Host': 'in.bookmyshow.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive'
}

DOWNLOAD_DELAY = 2.5


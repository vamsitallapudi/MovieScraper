# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import json
from re import I
from scrapy import signals, Request

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class MoviescraperDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


from urllib.parse import urlencode
from random import randint
import requests


class ScrapeOpsFakeUserAgentMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def __init__(self, settings):
        self.scrapeops_api_key = settings.get('SCRAPEOPS_API_KEY')
        self.scrapeops_endpoint = settings.get('SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT',
                                               'http://headers.scrapeops.io/v1/user-agents?')
        self.scrapeops_fake_user_agents_active = settings.get('SCRAPEOPS_FAKE_USER_AGENT_ENABLED', False)
        self.scrapeops_num_results = settings.get('SCRAPEOPS_NUM_RESULTS')
        self.headers_list = []
        self._get_user_agents_list()
        self._scrapeops_fake_user_agents_enabled()

    def _get_user_agents_list(self):
        payload = {'api_key': self.scrapeops_api_key}
        if self.scrapeops_num_results is not None:
            payload['num_results'] = self.scrapeops_num_results
        response = requests.get(self.scrapeops_endpoint, params=urlencode(payload))
        json_response = response.json()
        self.user_agents_list = json_response.get('result', [])

    def _get_random_user_agent(self):
        random_index = randint(0, len(self.user_agents_list) - 1)
        return self.user_agents_list[random_index]

    def _scrapeops_fake_user_agents_enabled(self):
        if self.scrapeops_api_key is None or self.scrapeops_api_key == '' or self.scrapeops_fake_user_agents_active == False:
            self.scrapeops_fake_user_agents_active = False
        else:
            self.scrapeops_fake_user_agents_active = True

    def process_request(self, request, spider):
        random_user_agent = self._get_random_user_agent()
        request.headers['User-Agent'] = random_user_agent

        print("************ NEW HEADER ATTACHED *******")
        print(request.headers['User-Agent'])


class ScrapeOpsFakeBrowserHeaderAgentMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def __init__(self, settings):
        self.scrapeops_api_key = settings.get('SCRAPEOPS_API_KEY')
        self.scrapeops_endpoint = settings.get('SCRAPEOPS_FAKE_BROWSER_HEADER_ENDPOINT',
                                               'http://headers.scrapeops.io/v1/browser-headers')
        self.scrapeops_fake_browser_headers_active = settings.get('SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED', True)
        self.scrapeops_num_results = settings.get('SCRAPEOPS_NUM_RESULTS')
        self.headers_list = []
        self._get_headers_list()
        self._scrapeops_fake_browser_headers_enabled()

    def _get_headers_list(self):
        payload = {'api_key': self.scrapeops_api_key}
        if self.scrapeops_num_results is not None:
            payload['num_results'] = self.scrapeops_num_results
        response = requests.get(self.scrapeops_endpoint, params=urlencode(payload))
        json_response = response.json()
        self.headers_list = json_response.get('result', [])

    def _get_random_browser_header(self):
        random_index = randint(0, len(self.headers_list) - 1)
        return self.headers_list[random_index]

    def _scrapeops_fake_browser_headers_enabled(self):
        if self.scrapeops_api_key is None or self.scrapeops_api_key == '' or self.scrapeops_fake_browser_headers_active == False:
            self.scrapeops_fake_browser_headers_active = False
        else:
            self.scrapeops_fake_browser_headers_active = True

    def process_request(self, request, spider):
        random_browser_header = self._get_random_browser_header()

        request.headers['accept-language'] = 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'
        request.headers['cache-control'] = 'max-age=0'
        request.headers['sec-fetch-user'] = random_browser_header['sec-fetch-user']
        request.headers['sec-fetch-mod'] = random_browser_header['sec-fetch-mod']
        request.headers['sec-fetch-site'] = random_browser_header['sec-fetch-site']
        request.headers['sec-ch-ua-platform'] = random_browser_header['sec-ch-ua-platform']
        request.headers['sec-ch-ua-mobile'] = random_browser_header['sec-ch-ua-mobile']
        request.headers['sec-ch-ua'] = random_browser_header['sec-ch-ua']
        request.headers['Cookie'] = 'G_AUTHUSER_H=0; _cfuvid=FMcy5rSmaph9JZTg7uCPskeGN_Zg7WvtofTrtEKBQD4-1702185861886-0-604800000; WZRK_G=c9a3b7fe33ab4259984502ba58098919; _gcl_au=1.1.340894221.1702185863; _ga=GA1.1.1013980103.1702185864; cf_clearance=O5Z3Tlgd79HpQQRLR4tvCqEdYWSMm5fnV.EE_jVAMW4-1702185863-0-1-e2ec13c5.f0e21527.a77b70ef-0.2.1702185863; __cfruid=03b3ed899125c03faad6b7a486396ee8626d4a9b-1702185864; AMP_TOKEN=%24NOT_FOUND; tvc_bmscookie=GA1.2.1013980103.1702185864; tvc_bmscookie_gid=GA1.2.759822804.1702185866; rgn=%7B%22Lat%22%3A%2217.385044%22%2C%22Seq%22%3A%224.0%22%2C%22Long%22%3A%2278.486671%22%2C%22regionName%22%3A%22Hyderabad%22%2C%22regionCode%22%3A%22HYD%22%2C%22isOlaEnabled%22%3A%22N%22%2C%22regionCodeSlug%22%3A%22hyd%22%2C%22regionNameSlug%22%3A%22hyderabad%22%2C%22GeoHash%22%3A%22tep%22%7D; G_ENABLED_IDPS=google; bmsId=1.774277133.1702185933098; __cf_bm=HLL5b3IZy3P_lFkEzeSkAbj45foJghFnNHLNsJkCYtc-1702188749-1-AaAHVzq+UacQyVGZXrwLjUZRPiHrv9mNKvFOIQsQ+QSaI8OH6pSsFyfX6eDBAAy0RdwlAItY3NguSonWABy949U=; preferences=%7B%22ticketType%22%3A%22M-TICKET%22%7D; WZRK_S_RK4-47R-98KZ=%7B%22p%22%3A12%2C%22s%22%3A1702187834%2C%22t%22%3A1702188796%7D; _ga_84T5GTD0PC=GS1.1.1702185863.1.1.1702188796.50.0.0'
        request.headers['accept'] = random_browser_header['accept']
        request.headers['user-agent'] = random_browser_header['user-agent']
        request.headers['upgrade-insecure-requests'] = random_browser_header.get('upgrade-insecure-requests')

        print("************ NEW HEADER ATTACHED *******")
        print(request.headers)


class ScrapeOpsProxyMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def __init__(self, settings):
        self.scrapeops_api_key = settings.get('SCRAPEOPS_API_KEY')
        self.scrapeops_endpoint = 'https://proxy.scrapeops.io/v1/?'
        self.scrapeops_proxy_active = settings.get('SCRAPEOPS_PROXY_ENABLED', False)

    @staticmethod
    def _param_is_true(request, key):
        if request.meta.get(key) or request.meta.get(key, 'false').lower() == 'true':
            return True
        return False

    @staticmethod
    def _replace_response_url(response):
        real_url = response.headers.get(
            'Sops-Final-Url', def_val=response.url)
        return response.replace(
            url=real_url.decode(response.headers.encoding))

    def _get_scrapeops_url(self, request):
        payload = {'api_key': self.scrapeops_api_key, 'url': request.url}
        if self._param_is_true(request, 'sops_render_js'):
            payload['render_js'] = True
        if self._param_is_true(request, 'sops_residential'):
            payload['residential'] = True
        if self._param_is_true(request, 'sops_keep_headers'):
            payload['keep_headers'] = True
        if request.meta.get('sops_country') is not None:
            payload['country'] = request.meta.get('sops_country')
        proxy_url = self.scrapeops_endpoint + urlencode(payload)
        print(f"proxy_url: {proxy_url}")
        return proxy_url

    def _scrapeops_proxy_enabled(self):
        if self.scrapeops_api_key is None or self.scrapeops_api_key == '' or self.scrapeops_proxy_active == False:
            return False
        return True

    def process_request(self, request, spider):
        if self._scrapeops_proxy_enabled is False or self.scrapeops_endpoint in request.url:
            return None

        scrapeops_url = self._get_scrapeops_url(request)
        new_request = request.replace(
            cls=Request, url=scrapeops_url, meta=request.meta)
        print(f"new_request: {new_request}")
        return new_request

    def process_response(self, request, response, spider):
        new_response = self._replace_response_url(response)
        return new_response

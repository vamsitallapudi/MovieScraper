import os
import smtplib

import scrapy

from MovieScraper.items import AmazonScraperItem


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains=['amazon.in']
    url = "https://www.amazon.in/gp/bestsellers/electronics/ref=zg_bs_nav_electronics_0"
    def start_requests(self):
        print("starting request")
        yield scrapy.Request(self.url, callback=self.parse)

    def parse(self, response):
        for movie_selector in response.css('._cDEzb_p13n-sc-css-line-clamp-3_g3dy1::text').extract():
            item = AmazonScraperItem()
            item['product_title'] = movie_selector
            yield item

    def send_mail(msg):
        email = os.environ.get("email")
        password = os.environ.get("password")
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(email, password)
        s.sendmail(email, "mail4vamsikrishna@gmail.com", msg)
        s.quit()
        print(msg)
        print("Sent")
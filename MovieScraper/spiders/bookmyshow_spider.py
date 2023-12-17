import os
import smtplib
import scrapy

from MovieScraper.items import PaytmScraperItem
from MovieScraper.settings import CUSTOM_HEADERS


class BookMyShowSpider(scrapy.Spider):
    name = 'bookmyshow'
    book_tickets = "Book tickets"
    url = "https://in.bookmyshow.com/explore/home/hyderabad"

    def start_requests(self):
        print("starting request")
        request = scrapy.Request(self.url, headers=CUSTOM_HEADERS, callback=self.parse)
        print(request)
        yield request

    def parse(self, response, **kwargs):
        print(f"Total response from {response}")
        for movie_selector in response.css('#bGbeea::text').extract():
            item = PaytmScraperItem()
            item['title'] = movie_selector
            if item.title == self.book_tickets:
                print(f"Book Tickets button for movie {self.movie} enabled. Sending Email")
                self.send_mail(msg="Hey Vamsi! Movie tickets for Animal are now available")
            yield item

    @staticmethod
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

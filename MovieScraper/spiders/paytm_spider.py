import os
import smtplib
from email.message import EmailMessage

import scrapy

from MovieScraper.items import PaytmScraperItem

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class BookMyShowSpider(scrapy.Spider):
    name = 'paytm'
    movie = "Dead"
    allowed_domains = ['paytm.com']
    url = "https://paytm.com/movies/hyderabad"

    def start_requests(self):
        print("starting request")
        request = scrapy.Request(self.url, callback=self.parse)
        print(request)
        yield request

    def parse(self, response, **kwargs):
        print(f"Total response from {response}")
        for movie_selector in response.css('.H5RunningMovieV2_movieName__XlSnn::text').extract():
            item = PaytmScraperItem()
            item['title'] = movie_selector
            if str.casefold(self.movie) in str.casefold(movie_selector):
                print("Movie is now available")
                print(f"Book Tickets button for movie {movie_selector} enabled. Sending Email")
                subject = "Tickets for " + movie_selector + " are Available"
                self.send_mail(subject=subject,
                               body="Hey Vamsi! Movie tickets for " + movie_selector + " are now available in Paytm")
            yield item

    def send_mail(self, subject, body):
        email = os.environ.get('EMAIL')
        password = os.environ.get('PASSWORD')
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = email
        msg['To'] = os.environ.get('EMAIL_TO')
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(email, password)
        s.send_message(msg)
        s.quit()
        print(msg)
        print("Sent")

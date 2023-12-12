import asyncio
import os
import smtplib
import time
from email.message import EmailMessage

import schedule
import scrapy
from dotenv import load_dotenv
from scrapy import cmdline

from MovieScraper.items import PaytmScraperItem

load_dotenv()

class PaytmSpider(scrapy.Spider):
    name = 'paytm'
    movie = "Sal"
    allowed_domains = ['paytm.com']
    start_urls = ["https://paytm.com/movies/hyderabad"]

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

def crawl_paytm():
    cmdline.execute("scrapy runspider PaytmSpider.py".split())

# Schedule the spider to run every 10 seconds
schedule.every(10).seconds.do(crawl_paytm)

# Run the scheduler
while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except KeyboardInterrupt:
        # Handle keyboard interrupt (e.g., Ctrl+C) to gracefully exit the loop
        break
    except Exception as e:
        # Handle other exceptions to prevent the scheduler from stopping
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()
        time.sleep(1)

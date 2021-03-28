from django.core.management.base import BaseCommand
from django.utils import timezone
from scrapers.amazon.main import ScraperAmazon
from chatbotweb.models import ScraperCookieCatcher

import datetime

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        cookies = ScraperAmazon.runBrowser()

        ScraperCookieCatcher.objects.create(cookies_data=cookies,catching_date=datetime.datetime.now())

        print("done!")
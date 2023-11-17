from scrapper.spider.location_spider import LocationSpider
from scrapper.spider.character_spider import CharacterSpider
import requests

# to run this script use:
# python manage.py shell < scrap.py

# Don't change order of starting requests
LocationSpider().start_requests()
CharacterSpider().start_requests()

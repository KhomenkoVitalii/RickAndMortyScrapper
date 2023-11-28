from scrapper.spider import location_spider, character_spider, episode_spider

import requests

# to run this script use:
# python manage.py shell < scrap.py

# Don't change order of starting requests
location_spider.LocationSpider().start_requests()
character_spider.CharacterSpider().start_requests()
episode_spider.EpisodeSpider().start_requests()

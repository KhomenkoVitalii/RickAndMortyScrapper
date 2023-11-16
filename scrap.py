from scrapper.spider.location_spider import LocationSpider

# to run this script use:
# python manage.py shell < scrap.py

LocationSpider().start_requests()

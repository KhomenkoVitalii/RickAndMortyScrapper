from django.core.management.base import BaseCommand, CommandError
from scrapper.spider import location_spider, character_spider, episode_spider


class Command(BaseCommand):
    help = "Starts process of scrapping data"

    def handle(self, *args, **options):
        # Don't change order of starting requests
        location_spider.LocationSpider().start_requests()
        character_spider.CharacterSpider().start_requests()
        episode_spider.EpisodeSpider().start_requests()

        self.stdout.write(
            self.style.SUCCESS('Successfully scrapped!')
        )

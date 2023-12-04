import requests
from scrapper.serializer import LocationSerializer
from scrapper.spider.spider import Spider


class LocationSpider(Spider):
    base_url = 'https://rickandmortyapi.com/api/location/'

    def parse(self, data):
        locations = data['results']

        for location_data in locations:
            serializer = LocationSerializer(data=location_data)
            if serializer.is_valid():
                location_instance = serializer.save()
                print(f"Saved Location: {location_instance.name}")
            else:
                print(f"Invalid data: {serializer.errors}")

        # Check for pagination
        next_page = data['info']['next']
        if next_page:
            response = requests.get(next_page)
            if response.status_code == 200:
                self.parse(response.json())

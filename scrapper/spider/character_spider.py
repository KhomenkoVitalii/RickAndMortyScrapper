import requests
from scrapper.models import Character, Location, Origin
from django.core.files.base import ContentFile
from rest_framework import response as rest_response
from scrapper.spider.spider import Spider
from RickAndMortyScrapper.settings import PUBLIC_IP


class CharacterSpider(Spider):
    base_url = 'https://rickandmortyapi.com/api/character/'
    URL = f"{PUBLIC_IP}/api/v1/character/"

    def download_image(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"Error while fetching image by url {url}: {e}")
            raise requests.exceptions.RequestException

    def try_parse_image(self, character_instance, image_url):
        try:
            image_content = self.download_image(image_url)
            if image_content:
                image_file = ContentFile(
                    image_content, name=f"character_{character_instance.name}_{character_instance.species or 'ordinary'}.jpg")
                character_instance.image.save(
                    image_file.name, image_file, save=True)
                print(
                    f"Saved Character: {character_instance.name} with image")
            else:
                print(
                    f"Failed to download image for Character: {character_instance.name}")
        except requests.exceptions.ConnectionError:
            print(f"Connection error: {e}")
        except requests.exceptions.TooManyRedirects:
            print(f"Too many redirects: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")

    def create_character_origin(self, character, character_data):
        # create character origin
        url = character_data['origin']['url']
        if not url:
            return

        response = requests.get(url)
        if response.status_code != 200:
            return

        origin_data = response.json()
        if origin_data['name']:
            location = Location.objects.get(name=origin_data['name'])
            Origin.objects.create(
                name=origin_data['name'], url=origin_data['url'], character_id=character, location=location).save()
        else:
            Origin.objects.create(
                name='unknown', url='', character_id=character).save()

    def save_character(self, character_data):
        # Create an instance of the model
        character_instance = Character()

        character_instance.name = character_data.get('name')
        character_instance.status = character_data.get('status')
        character_instance.species = character_data.get('species')
        character_instance.type = character_data.get('type')
        character_instance.gender = character_data.get('gender')
        character_instance.url = f"{self.URL}{character_data.get('id')}/"
        character_instance.created = character_data.get('created')

        try:
            location = Location.objects.get(
                name=character_data['location']['name'])
            character_instance.location = location
        except Location.DoesNotExist:
            character_instance.location = None

        # Download and save the image
        image_url = character_data.get('image')
        self.try_parse_image(character_instance, image_url)

        # Save the model instance to the database
        character_instance.save()

        self.create_character_origin(
            character=character_instance, character_data=character_data)

    def parse(self, data):
        characters = data['results']

        for character_data in characters:
            self.save_character(character_data)

        # Check for pagination
        next_page = data['info']['next']
        if next_page:
            response = requests.get(next_page)
            if response.status_code == 200:
                self.parse(response.json())

import requests
from scrapper.models import Episode, Character
from django.core.files.base import ContentFile
from scrapper.spider.spider import Spider
from RickAndMortyScrapper.settings import PUBLIC_IP


class EpisodeSpider(Spider):
    base_url = 'https://rickandmortyapi.com/api/episode/'
    URL = f"{PUBLIC_IP}/api/episode/"

    def assign_characters_to_the_episode(self, episode, characters_urls):
        for character_url in characters_urls:
            character_data = self.get_character(character_url)
            try:
                url = f"{PUBLIC_IP}/api/character/{character_data['id']}/"
                print(url)

                character = Character.objects.get(
                    url=url,
                )
            except Character.DoesNotExist:
                print(f"Character {character_data['name']} doesn't exist!")
                continue
            else:
                # add character to the episode
                episode.characters.add(character)

    def get_character(self, character_url):
        # make request
        response = requests.get(character_url)
        if not response.status_code == 200:
            print(
                f"Error while fetching character: {response.status_code}")
            raise response.raise_for_status()

        # retrieve character object or create if it doesn't exist
        return response.json()

    def save_episode(self, episode_data):
        # Create an instance of the model
        episode_instance = Episode()

        episode_instance.name = episode_data.get('name')
        episode_instance.air_date = episode_data.get('air_date')
        episode_instance.episode = episode_data.get('episode')
        episode_instance.url = f"{self.URL}{episode_data.get('id')}/"
        episode_instance.created = episode_data.get('created')

        # Save the model instance to the database
        episode_instance.save()

        return episode_instance

    def parse(self, data):
        episodes = data['results']

        for episode_data in episodes:
            episode_instance = self.save_episode(episode_data)

            print(f"Created episode {episode_data['episode']}")

            characters_urls = episode_data['characters']

            self.assign_characters_to_the_episode(
                episode=episode_instance, characters_urls=characters_urls)

            print(
                f"Finished assign character to the episode {episode_data['episode']}")

        # Check for pagination
        next_page = data['info']['next']
        if next_page:
            response = requests.get(next_page)
            if response.status_code == 200:
                self.parse(response.json())

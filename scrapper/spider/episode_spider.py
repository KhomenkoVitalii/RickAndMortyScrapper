import requests
from scrapper.models import Episode, Character
from django.core.files.base import ContentFile


class EpisodeSpider:
    base_url = 'https://rickandmortyapi.com/api/episode/'

    def start_requests(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            self.parse(response.json())

    def find_and_assign_characters_to_the_episode(self, episode, characters_urls):
        for character_url in characters_urls:
            # make request
            response = requests.get(character_url)
            if response.status_code == 200:
                # retrieve character object or create if it doesn't exist
                character_data = response.json()
                try:
                    character = Character.objects.get(
                        url=character_data.get('url'),
                    )
                except Character.DoesNotExist:
                    print(f"Character {character_data['name']} doesn't exist!")
                    continue
                else:
                    # add character to the episode
                    episode.characters.add(character)

    def parse(self, data):
        episodes = data['results']

        for episode_data in episodes:
            # Create an instance of the model
            episode_instance = Episode()

            episode_instance.name = episode_data.get('name')
            episode_instance.air_date = episode_data.get('air_date')
            episode_instance.episode = episode_data.get('episode')
            episode_instance.url = episode_data.get('url')
            episode_instance.created = episode_data.get('created')

            # Save the model instance to the database
            episode_instance.save()
            print(f"Created episode {episode_data['episode']}")

            characters_urls = episode_data['characters']

            self.find_and_assign_characters_to_the_episode(
                episode=episode_instance, characters_urls=characters_urls)

            print(
                f"Finished assign character to the episode {episode_data['episode']}")

        # Check for pagination
        next_page = data['info']['next']
        if next_page:
            response = requests.get(next_page)
            if response.status_code == 200:
                self.parse(response.json())

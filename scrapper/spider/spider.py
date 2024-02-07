import requests


class Spider:
    base_url = ""

    def start_requests(self):
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            self.parse(response.json())
        except requests.exceptions.RequestException as e:
            print(f"Error making initial request: {e}")

    def parse(self):
        raise NotImplementedError

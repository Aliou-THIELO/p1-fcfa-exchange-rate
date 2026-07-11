import requests
import os
from urllib3.util import Retry
from requests.adapters import HTTPAdapter
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("API_token")


class ExchangeRateClient:

    def __init__(self, base: str, token: str):
        self.base = base
        self.token = token

        self.session = requests.Session()
        retry = Retry(total=3,
              backoff_factor=1,
              status_forcelist=[500, 501, 502, 503])
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("https://", adapter)

    def _appel(self, endpoint: str, param: dict) -> dict:
        url = f"{self.base}/{self.token}/{endpoint}"

        try:
            response = self.session.get(url, params=param, timeout=10)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as e:
            print(f"Server error: {e}")
        except requests.exceptions.ConnectionError as e:
            print(f"Connection error: {e}")
        except requests.exceptions.Timeout as e:
            print(f"Server took too long to respond: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Exception error: {e}")

    def get_latest_rates(self, base_currency: str):
        return self._appel(f"latest/{base_currency}", param={})
    
if __name__ == "__main__":
    client = ExchangeRateClient("https://v6.exchangerate-api.com/v6", token)
    result = client.get_latest_rates("USD")
    print(result)
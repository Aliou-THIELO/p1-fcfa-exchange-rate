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
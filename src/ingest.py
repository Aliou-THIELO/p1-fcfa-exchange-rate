import requests
import os
from urllib3.util import Retry
from requests.adapters import HTTPAdapter
from dotenv import load_dotenv
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
log = logging.getLogger(__name__)


class APIError(Exception):
    pass
class AuthError(APIError):
    pass
class NotFoundError(APIError):
    pass
class ServerError(APIError):
    pass


class ExchangeRateClient:

    def __init__(self, base: str, token: str):
        self.base = base
        self.token = token

        self.session = requests.Session()
        retry = Retry(total=3,
              backoff_factor=1,
              status_forcelist=[429, 500, 501, 502, 503])
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("https://", adapter)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()

    def _appel(self, endpoint: str, param: dict) -> dict:
        url = f"{self.base}/{self.token}/{endpoint}"

        try:
            response = self.session.get(url, params=param, timeout=10)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as e:
            code = e.response.status_code
            if code in (401, 403):
                raise AuthError(f"Access denied: {code}") from e
            elif code == 404:
                raise NotFoundError(f"Resource not found: {code}") from e
            elif 500 <= code < 600:
                raise ServerError(f"Server error: {code}") from e
            else:
                raise APIError(f"Unexpected API error: {code}") from e
        except requests.exceptions.Timeout:
            raise APIError(f"Timeout.") from None
        except requests.exceptions.ConnectionError:
            raise APIError(f"Connection error.") from None

    def get_latest_rates(self, base_currency: str):
        return self._appel(f"latest/{base_currency}", param={})


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("API_token")

    if not token:
        raise ValueError("API_token is missing. Please set it in your .env file.")

    try:
        with ExchangeRateClient("https://v6.exchangerate-api.com/v6", token) as client:
            result = client.get_latest_rates("USD")
            print(result)

    except AuthError as e:
        log.error(f"Error Authorization: {e}")
    except NotFoundError as e:
        log.error(f"Not found: {e}")
    except ServerError as e:
        log.error(f"Server error: {e}")
    except APIError as e:
        log.error(f"API error: {e}")

# the session is already closed automatically
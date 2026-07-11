import requests
import os
from urllib3.util import Retry
from requests.adapters import HTTPAdapter
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("API_token")


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
            code = e.response.status_code
            if 400 <= code <= 403:
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
    try:
        client = ExchangeRateClient("https://v6.exchangerate-api.com/v6", token)
        result = client.get_latest_rates("USD")
        print(result)

    except AuthError as e:
        print(f"Error Authorization: {e}")
    except NotFoundError as e:
        print(f"Not found: {e}")
    except ServerError as e:
        print(f"Server error: {e}")
    except APIError as e:
        print(f"API error: {e}")
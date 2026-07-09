import requests
import os
from dotenv import load_dotenv
from urllib3.util import Retry
from requests.adapters import HTTPAdapter

load_dotenv()
token = os.getenv("API_token")

with requests.Session() as session:
    retry = Retry(total = 3,
              backoff_factor= 1,
              status_forcelist=[500, 501,502 ,503])
    adapter = HTTPAdapter (max_retries = retry)
    session.mount("https://", adapter)
    
    try :
        response = session.get(f"https://v6.exchangerate-api.com/v6/{token}/latest/USD", timeout= 10)
        response.raise_for_status()
        result = response.json()
        print(result)
    
    except requests.exceptions.HTTPError as e:
        print(f"Server error: {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error: {e}")
    except requests.exceptions.Timeout as e:
        print(f"Server took too long to respond: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Exception error: {e}")




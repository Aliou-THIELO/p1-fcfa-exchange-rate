import requests
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("API_token")

try :
    reponse = requests.get(f"https://v6.exchangerate-api.com/v6/{token}/latest/USD")
    reponse.raise_for_status()
    result = reponse.json()
    print(result)

except requests.exceptions.HTTPError as e:
    print(f" Erreur Serveur : {e}")
except requests.exceptions.ConnectionError:
    print(f" Probleme de connexion .")
except requests.exceptions.Timeout:
    print(f"Serveur trop lent .")
except requests.exceptions.RequestException as e:
    print(f" Erreur quelconque : {e}")
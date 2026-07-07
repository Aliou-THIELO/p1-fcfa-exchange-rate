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
    print(f"Erreur serveur : {e}")
except requests.exceptions.ConnectionError as e:
    print(f"Problème de connexion : {e}")
except requests.exceptions.Timeout as e:
    print(f"Le serveur a mis trop de temps à répondre : {e}")
except requests.exceptions.RequestException as e:
    print(f"Erreur inattendue : {e}")
import requests
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("API_token")

reponse = requests.get(f"https://v6.exchangerate-api.com/v6/{token}/latest/XOF")
result = reponse.json()
print(result)
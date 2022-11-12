import requests
from src.urls import *
import json

result = requests.get(url)
response = result.json()

print(response["id"])
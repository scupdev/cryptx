import requests
from api import create_app
from src.urls import *
import json

# result = requests.get(url)
# response = result.json()

# print(response["id"])

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
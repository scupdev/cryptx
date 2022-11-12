from flask import Blueprint
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def base():
    data = [
        {
            "name": "bitcoin",
            "symbol": "BTC",
            "price": 10000
        },
        {
            "name": "ethereum",
            "symbol": "ETH",
            "price": 10000
        }
    ]
    json_dump = json.dumps(data)
    return json_dump
from flask import Blueprint
from .request import Request
from .urls import *
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def base():
    request = Request()
    data = [
        {
            "name": "bitcoin",
            "symbol": "BTC",
            "price": request.send_request(bitcoin) 
        },
        {
            "name": "ethereum",
            "symbol": "ETH",
            "price": request.send_request(ethereum)
        },
        {
            "name": "solana",
            "symbol": "SOL",
            "price": request.send_request(solana)
        },
        {
            "name": "dogecoin",
            "symbol": "DOGE",
            "price": request.send_request(dogecoin)
        }
    ]
    json_dump = json.dumps(data)
    return json_dump
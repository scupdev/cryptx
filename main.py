from api import create_app
from src.request import send_request
from src.urls import *

if __name__ == "__main__":
    # app = create_app()
    # app.run(debug=True)

    # request
    print(send_request(bitcoin))
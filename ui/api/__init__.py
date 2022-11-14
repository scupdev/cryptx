# get requests from api

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from .xpath import xpath

class Request:
    def __init__(self):
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.options.add_argument('--headless')
        
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)

    def send_request(self, coin: str):
        self.browser.get(coin)
        while True:
            results = self.browser.find_elements('xpath', xpath)
            for result in results:
                return result.get_attribute('innerHTML')

# get requests from api
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from .xpath import xpath

def send_request(coin: str):
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument('--headless')

    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    browser.get(coin)
    results = browser.find_elements('xpath', xpath)

    for result in results:
        return result.get_attribute('innerHTML')

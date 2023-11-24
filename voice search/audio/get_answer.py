
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
from urllib.parse import urlparse
from bs4 import BeautifulSoup

class Fetcher:
    def __init__(self, url):
        self.url = url
        self.driver = None

    def lookup(self):
        # Your existing code for fetching the web page using Selenium
        self.driver = webdriver.Chrome()
        self.driver.wait = WebDriverWait(self.driver, 5)
        self.driver.get(self.url)
        
        # Get the page source after loading
        page_source = self.driver.page_source

        # Extract information using a separate method
        answer = self.extract_information(page_source)

        # Close the Selenium driver

        self.driver.quit()

        return answer

    def extract_information(self, page_source):
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(page_source, "html.parser")

        # Find the span element by class and id (customize this based on your needs)
        span_element = soup.find('span', class_='wob_t', id='wob_tm')

        # Check if the span element was found
        if span_element:
            # Extract and return the text content of the span element
            return span_element.text
        else:
            return "I don't know."




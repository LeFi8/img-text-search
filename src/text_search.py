import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TextSearch:
    def __init__(self):
        self._service = Service()
        self._options = webdriver.ChromeOptions()
        self._options.add_argument('--no-sandbox')
        # self._options.add_argument("--window-size=1920,1080")
        self._options.add_argument('--disable-dev-shm-usage')
        self._options.add_experimental_option("detach", True)
        self._driver = webdriver.Chrome(
            service=self._service, options=self._options)

    def text_search(self, text: str):
        print(f"Searching for: \n {text}")

        self._driver.get("https://google.com/")

        element = self._driver.find_element("xpath", "//button[@id='W0wltc']")
        ActionChains(self._driver).move_to_element(
            element).perform()
        element.click()

        search_input = self._driver.find_element(By.NAME, "q")
        search_input.send_keys(text)

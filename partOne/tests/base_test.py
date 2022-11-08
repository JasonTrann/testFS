import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
import undetected_chromedriver as uc


class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        # options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox')  # # Bypass OS security model
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument("--start-fullscreen")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-web-security')
        # options.add_argument('--user-data-dir=true')
        options.add_argument('--allow-running-insecure-content')

        self.driver = uc.Chrome(options=options)
        self.driver.get("https://fundingsocieties.com/")
        stealth(self.driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )

    def tearDown(self):
        self.driver.close()

import unittest

from tests.base_test import BaseTest
from pages.home_page import *
from pages.statistics_page import *
from time import sleep


class TestSignInPage(BaseTest):

    def test_web_site(self):
        statistics_page = StatisticsPage(self.driver)
        home_page = HomePage(self.driver)

        # Question 1:
        home_page.is_home_page_displayed()

        # Question 2:
        home_page.click_statistics_tab()

        # Question 3 & 4:
        statistics_page.is_statistics_page_displayed()
        
        statistics_page.total_fund()
        sleep(5)


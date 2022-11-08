from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException


class StatisticsPage(BasePage):
    TOTAL_FUNDED_VALUE = (By.XPATH, "//div[normalize-space()='Total funded']/preceding-sibling::font")
    NO_OF_FINANCING_VALUE = (By.XPATH, "//div[@class='statisticDetailRow']//div[1]//div[1]/preceding-sibling::font")
    DEFAULT_RATE_VALUE = (By.XPATH, "(//div[@class='detailNumber text-center'])[3]/font")
    FINANCING_FULL_RATE_VALUE = (By.XPATH, "(//div[@class='detailNumber text-center'])[4]/font")
    GENERAL_TAB = (By.XPATH, "//button[normalize-space()='General']")
    REPAYMENT_TAB = (By.XPATH, "//button[normalize-space()='Repayment']")
    DISBURSEMENT_TAB = (By.XPATH, "//button[normalize-space()='Disbursement']")
    test1 = (By.XPATH, "(//*[name()='path'][@class='highcharts-point highcharts-color-0'])[32]")
    # test2 = (By.XPATH, "//*[@id="highcharts-ckczxsn-0"]/svg/g[8]/text/tspan[4]")
    test3 = (By.XPATH, "//span[normalize-space()='Tiếp theo']")

    def __init__(self, driver):
        super(StatisticsPage, self).__init__(driver)  # Python2 version

    def is_statistics_page_displayed(self):
        print("Check if Login Page is displayed")
        try:
            self.wait_element(*self.TOTAL_FUNDED_VALUE)
            self.wait_element(*self.NO_OF_FINANCING_VALUE)
            self.wait_element(*self.DEFAULT_RATE_VALUE)
            self.wait_element(*self.FINANCING_FULL_RATE_VALUE)
            self.wait_element(*self.GENERAL_TAB)
            self.wait_element(*self.REPAYMENT_TAB)
            self.wait_element(*self.DISBURSEMENT_TAB)
            return True
        except TimeoutException:
            return False

    def total_fund(self):
        total_text = self.find_element(By.XPATH, "//*[name()='text']//*[name()='tspan' and(contains(@style,'bold'))]").text
        print(total_text)



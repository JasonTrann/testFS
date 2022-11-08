from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    STATISTICS_TAB = (By.XPATH, "//div[contains(@role,'navigation')]//a[contains(@class,'t-l-base-gray-darker')][normalize-space()='Statistics']")
    START_INVEST_BTN = (By.XPATH, "//a[normalize-space()='Start investing']")
    GET_FINA_BTN = (By.XPATH, "//a[normalize-space()='Get financing']")
    SUBJECT_FIELD = (By.XPATH, "//input[@class='aoT'][@name='subjectbox']")
    BODY_FIELD = (By.XPATH, "//div[@class='Am Al editable LW-avf tS-tW']")
    SENT_BTN = (By.XPATH, "//div[@class='T-I J-J5-Ji aoO v7 T-I-atl L3']")

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def click_statistics_tab(self):
        print("CLick Statistics Tab Button")
        self.find_element(*self.STATISTICS_TAB).click()

    def is_home_page_displayed(self):
        print("Check if Home Page is displayed")
        try:
            self.wait_element(*self.START_INVEST_BTN)
            self.wait_element(*self.GET_FINA_BTN)
            return True
        except TimeoutException:
            return False


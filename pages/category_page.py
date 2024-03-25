from selenium.webdriver.common.by import By

from browser import Browser
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CategoryPage(BasePage):
    COMPUTERS_SELECTOR = (By.LINK_TEXT, 'Computers')
    SUBCATEGORIES_SELECTOR = (By.CSS_SELECTOR, '.item-box')

    def navigate_to_homepage(self):
        self.driver.get('https://demo.nopcommerce.com/')

    def click_on_category_button(self, category):
        category_element = self.get_element_by_link_text(category)
        category_element.click()

    def get_subcategories(self):
        return self.driver.find_elements(*self.SUBCATEGORIES_SELECTOR)

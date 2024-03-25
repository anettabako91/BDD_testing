from selenium.webdriver.common.by import By

from browser import Browser


class BasePage(Browser):

    def get_element_by_link_text(self, text):
        return self.driver.find_element(By.LINK_TEXT, text)

# daca pagina are link_text putem folosi aceasta metoda - este mult mai usor, scriem mult mai putin

from selenium.webdriver.common.by import By

from browser import Browser


class LoginPage(Browser):
    EMAIL_FIELD_SELECTOR = (By.CSS_SELECTOR, 'input.email')
    PASSWORD_FIELD_SELECTOR = (By.CSS_SELECTOR, 'input.password')
    LOGIN_BUTTON_SELECTOR = (By.CSS_SELECTOR, '.login-button')
    MESSAGE_ERROR_LABEL = (By.CSS_SELECTOR, '.message-error')
    EMAIL_ERROR_MESSAGE = (By.CSS_SELECTOR, '#Email-error')

    def navigate_to_login_page(self):
        self.driver.get('https://demo.nopcommerce.com/login')

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL_FIELD_SELECTOR).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD_SELECTOR).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON_SELECTOR).click()

    def get_error_message(self):
        return self.driver.find_element(*self.MESSAGE_ERROR_LABEL).text

    def get_email_error(self):
        return self.driver.find_element(*self.EMAIL_ERROR_MESSAGE).text

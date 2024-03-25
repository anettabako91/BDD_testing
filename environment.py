from browser import Browser
from pages.category_page import CategoryPage
from pages.login_page import LoginPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.CategoryPage = CategoryPage()


def after_all(context):
    context.browser.close

# astea de aici sunt ca si setup si teardown

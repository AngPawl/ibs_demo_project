import allure
from selene import browser, have


class CookiePage:
    def __init__(self):
        self.page_title = browser.element('.top h1')

    @allure.step('Cookie Page title should have correct name {name}')
    def page_title_should_have_correct_name(self, name):
        self.page_title.should(have.exact_text(name))

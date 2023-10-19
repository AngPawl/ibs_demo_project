import allure
from selene import browser, be


class Header:
    def __init__(self):
        self.context_menu = browser.element('.header-burger')
        self.logo = browser.element('.header-logo')
        self.searchbar_button = browser.element('a[class$="header-search"]')
        self.searchbar_input = browser.element('input[class$="search-input"]')

    @allure.step('Open Context Menu')
    def open_context_menu(self):
        self.context_menu.click()

    @allure.step('Context Menu button should be displayed')
    def context_menu_button_should_be_displayed(self):
        self.context_menu.should(be.clickable)

    @allure.step('Logo should render')
    def logo_should_render(self):
        self.logo.should(be.visible)

    @allure.step('Click on logo')
    def click_on_logo(self):
        self.logo.click()

    @allure.step('Type search query {query}')
    def type_search_query(self, query):
        self.searchbar_button.click()
        self.searchbar_input.send_keys(query).press_enter()

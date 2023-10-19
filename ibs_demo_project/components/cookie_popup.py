import allure
from selene import browser, be


class CookiePopup:
    def __init__(self):
        self.popup = browser.element('.cookies')
        self.details_button = browser.element('.cookies .cookies-left-read a')
        self.accept_button = browser.element('a[class$="cookies-close"]')

    @allure.step('Cookie Popup should render')
    def should_render(self):
        self.popup.should(be.visible)

    @allure.step('Cookie Popup should not render')
    def should_not_render(self):
        self.popup.should(be.not_.visible)

    @allure.step('Click on Details button')
    def click_on_details_button(self):
        self.details_button.click()

    @allure.step('Click on Details button')
    def click_on_accept_button(self):
        self.accept_button.click()

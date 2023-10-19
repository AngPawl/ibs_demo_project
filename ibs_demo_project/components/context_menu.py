import allure
from selene import browser, have, be


class ContextMenu:
    def __init__(self):
        self.titles = browser.all('.navigation-sections a:not(:last-child)')
        self.social_media_buttons = browser.all('.navigation-socials a')
        self.close_button = browser.element('.navigation-close')

    @allure.step('Titles should have correct names: {names}')
    def titles_should_have_correct_names(self, names):
        self.titles.should(have.exact_texts(names))

    @allure.step('Social media buttons should be displayed')
    def social_media_buttons_should_be_displayed(self):
        for button in self.social_media_buttons:
            button.should(be.clickable)

    @allure.step('Click on Close button')
    def click_on_close_button(self):
        self.close_button.click()

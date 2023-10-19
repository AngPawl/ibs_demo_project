import allure
from selene import browser

from config import config


class MainPage:
    @allure.step('User should be redirected to Main Page')
    def user_should_be_redirected_to_main_page(self):
        assert (
            browser.config.driver.current_url == config.base_url + '/'
        ), f"User is currently on {browser.config.driver.current_url}"

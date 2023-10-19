import allure
from selene import browser

from ibs_demo_project.components.context_menu import ContextMenu
from ibs_demo_project.components.cookie_popup import CookiePopup
from ibs_demo_project.components.header import Header
from ibs_demo_project.pages.cookie_page import CookiePage
from ibs_demo_project.pages.main_page import MainPage
from ibs_demo_project.pages.search_results_page import SearchResultsPage


class WebsiteManager:
    def __init__(self):
        self.main_page = MainPage()
        self.header = Header()
        self.context_menu = ContextMenu()
        self.cookie_popup = CookiePopup()
        self.cookie_page = CookiePage()
        self.search_results_page = SearchResultsPage()

    @staticmethod
    @allure.step('Open website')
    def open():
        browser.open('/')


website = WebsiteManager()

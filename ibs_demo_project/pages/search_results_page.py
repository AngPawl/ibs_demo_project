import allure
from selene import browser, have


class SearchResultsPage:
    def __init__(self):
        self.search_tabs = browser.all('.search-tabs a')
        self.all_results_tab = browser.element('.search-tabs a.is-active')

    @allure.step('All results tab should show the number of results not as (0)')
    def all_results_tab_should_show_number_of_results(self):
        self.all_results_tab.should(have.no.text('(0)'))

    @allure.step('All results tab should show the number of results as (0)')
    def all_results_tab_should_show_zero_number_of_results(self):
        self.all_results_tab.should(have.text('(0)'))

    @allure.step('Search tabs should render on the page')
    def search_tabs_should_render(self):
        self.search_tabs.should(have.size_greater_than(1))

    @allure.step('Search tabs should not render on the page')
    def search_tabs_should_not_ender(self):
        self.search_tabs.should(have.size(1))

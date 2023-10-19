import allure
from allure_commons.types import Severity

from ibs_demo_project.website import website


@allure.title('Search query should return results')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_search_query_should_return_results():
    website.open()

    website.header.type_search_query('python')

    website.search_results_page.search_tabs_should_render()
    website.search_results_page.all_results_tab_should_show_number_of_results()


@allure.title('Search query should not return results')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_search_query_should_not_return_results():
    website.open()

    website.header.type_search_query('abracadabra')

    website.search_results_page.search_tabs_should_not_ender()
    website.search_results_page.all_results_tab_should_show_zero_number_of_results()

import allure
from allure_commons.types import Severity

from ibs_demo_project.website import website


@allure.title('Logo should render in the header')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_header_logo_should_render():
    website.open()

    website.header.logo_should_render()


@allure.title('Logo button should redirect to the main page')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_header_logo_should_redirect_to_main_page():
    website.open()

    website.cookie_popup.click_on_details_button()

    website.header.click_on_logo()

    website.main_page.user_should_be_redirected_to_main_page()

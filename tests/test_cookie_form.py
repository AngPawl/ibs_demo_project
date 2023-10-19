import allure
from allure_commons.types import Severity

from ibs_demo_project.website import website


@allure.title('Cookie Popup renders on the page')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_cookie_popup_renders():
    website.open()

    website.cookie_popup.should_render()


@allure.title('Cookie Popup opens Cookie page')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_cookie_popup_opens_cookie_page():
    website.open()

    website.cookie_popup.click_on_details_button()

    website.cookie_page.page_title_should_have_correct_name('Сведения о сookies-файлах')


@allure.title('Cookie Popup closes after Accept button is pressed')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_cookie_popup_closes_after_accept_button_is_pressed():
    website.open()

    website.cookie_popup.click_on_accept_button()

    website.cookie_popup.should_not_render()

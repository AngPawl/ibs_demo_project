import allure
from allure_commons.types import Severity

from ibs_demo_project.website import website


@allure.title('Context Menu should have correct titles')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_context_menu_should_have_correct_titles():
    website.open()

    website.header.open_context_menu()

    website.context_menu.titles_should_have_correct_names(
        [
            'Решения и услуги',
            'Отраслевые решения',
            'Проекты',
            'Создано в IBS',
            'Карьера',
            'Медиацентр',
            'О компании',
        ]
    )


@allure.title('Context Menu should have social media buttons')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_context_menu_should_have_social_media_buttons():
    website.open()

    website.header.open_context_menu()

    website.context_menu.social_media_buttons_should_be_displayed()


@allure.title('Context Menu is successfully closed')
@allure.label('owner', 'AngPawl')
@allure.tag('smoke tests')
@allure.severity(Severity.CRITICAL)
def test_context_menu_is_successfully_closed():
    website.open()

    website.header.open_context_menu()
    website.context_menu.click_on_close_button()

    website.header.context_menu_button_should_be_displayed()

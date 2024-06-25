import allure
from conftest import *
from data import Urls
from pages.user_account_page import UserAccountPage
from pages.header_page import HeaderPage
from data import Text


class TestUserAccount:
    @allure.title('Проверка перехода в личный кабинет через кнопку "Личный кабинет" в шапке')
    def test_redirect_to_account_from_header(self, driver, login):
        uap = UserAccountPage(driver)
        uap.click_account_btn()
        assert uap.get_current_url() == Urls.PROFILE_PAGE

    @allure.title('Проверка перехода в раздел История заказов')
    def test_redirect_to_order_history(self, driver, login):
        uap = UserAccountPage(driver)
        uap.click_account_btn()
        uap.click_on_order_list()
        assert uap.get_current_url() == Urls.ORDERS_HISTORY

    @allure.title('Проверка выхода из аккаунта')
    def test_logout(self, driver, login):
        uap = UserAccountPage(driver)
        HeaderPage(driver).click_user_account_btn()
        uap.wait_visibility_profile_button()
        uap.click_logout_btn()
        uap.wait_visibility_enter_button()
        assert uap.get_text_enter_button() == Text.BUTTON_TEXT


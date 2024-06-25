import allure
from conftest import *
from data import Urls
from pages.user_account_page import UserAccountPage
from pages.password_recovery_page import PasswordRecoverPage
from pages.header_page import HeaderPage


class TestPasswordRecover:
    @allure.title('Проверка перехода по клику на кнопку Восстановить пароль на странице логина')
    def test_click_password_recover_button(self, driver):
        prp = PasswordRecoverPage(driver)
        HeaderPage(driver).click_user_account_btn()
        UserAccountPage(driver).click_password_recover_btn()
        prp.click_recover_btn()
        assert prp.find_save_button().is_displayed()

    @allure.title('Проверка перехода по кнопке Восстановить после ввода почты')
    def test_enter_email_and_click_recover(self, driver, create_and_delete_user):
        prp = PasswordRecoverPage(driver)
        prp.open_page(Urls.FORGOT_PASSWORD_PAGE)
        prp.set_email_for_recover_password(create_and_delete_user[0]['email'])
        prp.click_recover_btn()
        assert prp.find_save_button().is_displayed()

    @allure.title('Проверка активности поля пароль после клика по иконке показать/скрыть')
    def test_active_password_field(self, driver, create_and_delete_user):
        prp = PasswordRecoverPage(driver)
        prp.open_page(Urls.FORGOT_PASSWORD_PAGE)
        prp.set_email_for_recover_password(create_and_delete_user[0]['email'])
        prp.click_recover_btn()
        prp.find_save_button()
        prp.click_on_show_password_icon()
        assert prp.check_input_password_field()


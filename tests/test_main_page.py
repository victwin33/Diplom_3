import allure
from conftest import *
from pages.main_page import MainPage
from data import Text



class TestMainPage:
    @allure.title('Проверка появления всплывающее окна после клика по ингредиенту')
    def test_open_ingredient_popup(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_bun()
        popup_text = main_page.check_popup_text()
        assert popup_text == Text.POPUP_TEXT


    @allure.title('Проверка закрытия всплывающего окна ингредиента кликом по крестику')
    def test_close_ingredient_details_popup(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_bun()
        main_page.click_close_btn()
        main_page.check_invisibility_of_popup()
        assert main_page.check_invisibility_of_popup().is_displayed() == False


    @allure.title('Проверка изменения счетчика ингредиента')
    def test_change_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        start_quantity = main_page.check_counter_of_ingredients()
        main_page.add_filling_to_order_basket()
        end_quantity = main_page.check_counter_of_ingredients()
        assert end_quantity > start_quantity


    @allure.title('Проверка создания заказа')
    def test_make_order(self, driver, login):
        main_page = MainPage(driver)
        main_page.find_ingredient_bun()
        main_page.add_bun_to_order_basket()
        main_page.add_sauce_to_order_basket()
        main_page.click_order_btn()
        main_page.find_order_number()
        assert main_page.check_order_status().is_displayed()



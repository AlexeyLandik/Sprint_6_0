import allure
import pytest
from pages.order_page import OrderPage
from config import Config


class TestOrderPage:
    @pytest.mark.parametrize(
        "name, last_name, address, phone_number, date, comment",
        [
            (Config.NAME_1, Config.LAST_NAME_1, Config.ADDRESS_1, Config.PHONE_NUMBER_1, Config.DATE_1,
             Config.COMMENT_1),
            (Config.NAME_2, Config.LAST_NAME_2, Config.ADDRESS_2, Config.PHONE_NUMBER_2, Config.DATE_2,
             Config.COMMENT_2)
        ]
    )
    @allure.title('Тестируем флоу заказа самоката: 2 теста')
    def test_scooter_order(self, driver, name, last_name, address, phone_number, date, comment):
        order_page = OrderPage(driver)
        result = order_page.set_order(name, last_name, address, phone_number, date, comment)
        assert Config.POSITIVE_ORDER_STATUS in result

    @allure.title('Тестируем переход на главную страницу по лого Самокат: 1 тест')
    def test_scooter_logo_click(self, driver):
        order_page = OrderPage(driver)
        assert order_page.click_scooter_logo()

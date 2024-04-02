import allure
import pytest
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from config import Config


class TestMainPage:
    @pytest.mark.parametrize(
        'num, result',
        [
            (0, Config.ANSWER_TEXT_0),
            (1, Config.ANSWER_TEXT_1),
            (2, Config.ANSWER_TEXT_2),
            (3, Config.ANSWER_TEXT_3),
            (4, Config.ANSWER_TEXT_4),
            (5, Config.ANSWER_TEXT_5),
            (6, Config.ANSWER_TEXT_6),
            (7, Config.ANSWER_TEXT_7)
        ]
    )
    @allure.title('Тестируем Вопросы о важном: 8 тестов')
    def test_questions_and_answers(self, driver, result, num):  # driver - передается фикстура драйвера
        main_page = MainPage(driver)        # инициализация страницы делается внутри теста
        assert main_page.get_answer_text(num) == result

    @pytest.mark.parametrize(
        'locator_order_button',  # передаю локаторы в тест из-за параметризации, по совету наставника
        [
            MainPageLocators.ORDER_BUTTON_IN_HEADER_LOCATOR,
            MainPageLocators.ORDER_BUTTON_DOWN_LOCATOR
        ]
    )
    @allure.title('Тестируем кнопки Заказать: 2 теста')
    def test_order_buttons(self, driver, locator_order_button):
        main_page = MainPage(driver)
        assert main_page.main_order_button(locator_order_button) == Config.ORDER_TITLE_TEXT

    @allure.title('Тестируем редирект на Дзен по лого Яндекс: 1 тест')
    def test_yandex_logo_click(self, driver):
        main_page = MainPage(driver)
        assert main_page.click_yandex_logo() == Config.DZEN_URL



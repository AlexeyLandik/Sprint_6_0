import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Тестируем кнопку Вопросы о важном')
    def get_answer_text(self, num):
        self.click_cookie(MainPageLocators.COOKIE_BUTTON_LOCATOR)
        locator_q = MainPageLocators.QUESTION_LOCATOR
        locator_a = MainPageLocators.ANSWER_LOCATOR
        locator_q_formatted = self.format_locators(locator_q, num)
        locator_a_formatted = self.format_locators(locator_a, num)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Тестируем кнопку "Заказать" основной страницы')
    def main_order_button(self, locator_order_button):
        self.click_cookie(MainPageLocators.COOKIE_BUTTON_LOCATOR)
        self.click_to_element(locator=locator_order_button)
        return self.get_text_from_element(MainPageLocators.ORDER_TITLE_LOCATOR)

    @allure.step('Тестируем переход по логотипу Яндекс')
    def click_yandex_logo(self):
        self.click_to_element(MainPageLocators.LOGO_YANDEX_LOCATOR)
        return self.switch_page(MainPageLocators.LOGO_DZEN_LOCATOR, 1)

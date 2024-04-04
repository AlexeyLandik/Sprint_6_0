import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step('Тестируем переход на кнопку Заказа')
    def enter_to_order_page(self, locator_order_button):
        self.click_cookie(MainPageLocators.COOKIE_BUTTON_LOCATOR)
        self.click_to_element(locator=locator_order_button)

    @allure.step('Тестируем флоу Заказа')
    def set_order(self, name, last_name, address, phone_number, date, comment,):
        self.enter_to_order_page(MainPageLocators.ORDER_BUTTON_IN_HEADER_LOCATOR)
        self.add_text_to_element(OrderPageLocators.NAME_FIELD_LOCATOR, name)
        self.add_text_to_element(OrderPageLocators.LAST_NAME_FIELD_LOCATOR, last_name)
        self.add_text_to_element(OrderPageLocators.ADDRESS_FIELD_LOCATOR, address)
        self.click_to_element(OrderPageLocators.METRO_STATION_FIELD_LOCATOR)
        self.click_to_element(OrderPageLocators.METRO_STATION_DROP_DOWN_ITEM_LOCATOR)
        self.add_text_to_element(OrderPageLocators.PHONE_FIELD_LOCATOR, phone_number)
        self.click_to_element(OrderPageLocators.NEXT_BUTTON_LOCATOR)
        self.add_text_to_element(OrderPageLocators.DATE_FIELD_LOCATOR, date)
        self.click_to_element(OrderPageLocators.HEADER_SECOND_ORDER_FORM_LOCATOR)
        self.click_to_element(OrderPageLocators.RENT_TIME_FIELD_LOCATOR)
        self.click_to_element(OrderPageLocators.RENT_TIME_ITEM_LOCATOR)
        self.click_to_element(OrderPageLocators.COLOUR_LOCATOR)
        self.add_text_to_element(OrderPageLocators.COMMENT_LOCATOR, comment)
        self.click_to_element(OrderPageLocators.MAKE_ORDER_BUTTON_LOCATOR)
        self.click_to_element(OrderPageLocators.YES_BUTTON_LOCATOR)
        return self.get_text_from_element(OrderPageLocators.ORDER_STATUS_LOCATOR)

    @allure.step('Тестируем лого Самокат')
    def click_scooter_logo(self):
        self.enter_to_order_page(MainPageLocators.ORDER_BUTTON_IN_HEADER_LOCATOR)
        self.click_to_element(OrderPageLocators.HEADER_LOGO_SCOOTER_LOCATOR)
        return self.find_element_with_wait(MainPageLocators.MAIN_PAGE_TITLE_LOCATOR)




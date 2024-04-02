from selenium.webdriver.common.by import By


class OrderPageLocators:
    # поле Имя
    NAME_FIELD_LOCATOR = By.XPATH, './/*[@placeholder="* Имя"]/parent::div/input'
    # поле Фамилия
    LAST_NAME_FIELD_LOCATOR = By.XPATH, './/*[@placeholder="* Фамилия"]/parent::div/input'
    # поле Адрес
    ADDRESS_FIELD_LOCATOR = By.XPATH, './/*[@placeholder="* Адрес: куда привезти заказ"]/parent::div/input'
    # поле Телефон
    PHONE_FIELD_LOCATOR = By.XPATH, './/*[@placeholder="* Телефон: на него позвонит курьер"]/parent::div/input'
    # поле Станция метро
    METRO_STATION_FIELD_LOCATOR = By.XPATH, './/*[@placeholder="* Станция метро"]/parent::div'
    # выбор станции метро из выпадающего списка
    METRO_STATION_DROP_DOWN_ITEM_LOCATOR = By.XPATH, ".//*[(@class ='Order_SelectOption__82bhS select-search__option' and @value='5')]"
    # кнопка Далее
    NEXT_BUTTON_LOCATOR = By.XPATH, ".//*[@class='Order_NextButton__1_rCA']/button"
    # поле Когда привезти самокат
    DATE_FIELD_LOCATOR = By.XPATH, ".//*[@placeholder='* Когда привезти самокат']"
    # поле Срок аренды
    RENT_TIME_FIELD_LOCATOR = By.XPATH, ".//*[@class='Dropdown-root']"
    # время аренды
    RENT_TIME_ITEM_LOCATOR = By.XPATH, ".//*[text() = 'четверо суток']"
    # цвет самоката
    COLOUR_LOCATOR = By.XPATH, ".//*[text() = 'чёрный жемчуг']"
    # поле комментария
    COMMENT_LOCATOR = By.XPATH, ".//*[@placeholder='Комментарий для курьера']"
    # кнопка Заказать
    MAKE_ORDER_BUTTON_LOCATOR = By.XPATH, ".//button[contains(@class,'Button_Button__ra12g Button_Middle__1CSJM')]/following-sibling::button[1]"
    # кнопка Да
    YES_BUTTON_LOCATOR = By.XPATH, ".//*[text() = 'Да']"
    # статус заказа
    ORDER_STATUS_LOCATOR = By.XPATH, ".//*[contains(text(),'Заказ оформлен')]"
    # хедер второй страницы заказа
    HEADER_SECOND_ORDER_FORM_LOCATOR = By.XPATH, ".//*[@class='Order_Header__BZXOb']"
    # логотип Самокат
    HEADER_LOGO_SCOOTER_LOCATOR = By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']"

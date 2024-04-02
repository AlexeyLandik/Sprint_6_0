from selenium.webdriver.common.by import By


class MainPageLocators:
    # локатор для вопросов
    QUESTION_LOCATOR = By.XPATH, ".//*[@id='accordion__heading-{}']"
    # локатор для ответов
    ANSWER_LOCATOR = By.XPATH, ".//*[@id='accordion__panel-{}']"
    # кнопка куки
    COOKIE_BUTTON_LOCATOR = By.XPATH, './/*[@id="rcc-confirm-button"]'
    # кнопка Заказать в хедере
    ORDER_BUTTON_IN_HEADER_LOCATOR = By.CLASS_NAME, 'Button_Button__ra12g'
    # кнопка Заказать внизу страницы
    ORDER_BUTTON_DOWN_LOCATOR = By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]//button'
    # заголовок формы заказа "Для кого самокат"
    ORDER_TITLE_LOCATOR = By.CLASS_NAME, 'Order_Header__BZXOb'
    # заголовок главной страницы
    MAIN_PAGE_TITLE_LOCATOR = By.XPATH, ".//div[contains(text(),'Самокат')]"
    # логотип Яндекс на главной странице
    LOGO_YANDEX_LOCATOR = By.XPATH, './/*[@class="Header_LogoYandex__3TSOI"]'
    # логотип Дзен на Яндекс
    LOGO_DZEN_LOCATOR = By.XPATH, ".//*[@class='desktop-base-header__logoLink-aE']"


# pages/header_component.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Header(BasePage):
    # locator
    SEARCH_ICON = (By.CSS_SELECTOR,"button[data-gnb-kind='search']")
    LOGO = (By.CSS_SELECTOR,"a[aria-label='Wanted']")


    def __init__(self,driver):
        super().__init__(driver)

    def click_search_icon(self):
        # 검색 아이콘 클릭
        self.click(self.SEARCH_ICON)

    def click_logo(self):
        # 로고 클릭
        self.click(self.LOGO)

    def click_menu(self,menu_kind):
        # 메뉴 클릭
        locator = (By.CSS_SELECTOR, f"li[data-gnb-kind='{menu_kind}']")
        self.click(locator)
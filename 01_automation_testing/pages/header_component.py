# pages/header_component.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class Header(BasePage):
    # locator
    SEARCH_ICON = (By.CSS_SELECTOR,"button[data-gnb-kind='search']")
    LOGO = (By.CSS_SELECTOR,"a[aria-label='Wanted']")

    NAVBAR = (By.CSS_SELECTOR, "div[role='presentation']")
    HAMBURGER_MENU = (By.CSS_SELECTOR, "button[data-gnb-kind='more']")


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

    def is_hamburger_menu_visible(self):
        try:
            hamburger = self.find_element(self.HAMBURGER_MENU)
            return hamburger.is_displayed()
        except:
            return False
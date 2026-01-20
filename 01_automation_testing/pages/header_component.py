# pages/header_component.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Header(BasePage):
    # locator
    SEARCH_ICON = (By.CSS_SELECTOR,"button[data-gnb-kind='search']")


    def __init__(self,driver):
        super().__init__(driver)

    def click_search_icon(self):
        # 검색 아이콘 클릭
        self.click(self.SEARCH_ICON)
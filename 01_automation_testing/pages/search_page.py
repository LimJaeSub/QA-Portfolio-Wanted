# /pages/search_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

from selenium.webdriver.common.keys import Keys


"""
원티드는 검색 모달창하고 검색 결과 페이지가 두 개로 나뉘어짐
총 2개의 클래스를 생성해서 구현
"""

class SearchModal(BasePage):
    
    # locators
    SEARCH_ICON = (By.CSS_SELECTOR,"button[data-gnb-kind='search']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "[role='presentation'] input[type='search']")

    def __init__(self,driver):
        super().__init__(driver)

    def open_modal(self):
        # 검색 모달 오픈
        self.click(self.SEARCH_ICON)
        

    def is_modal_visible(self):
        # 모달 보이는지 확인
        return self.is_element_visible(self.SEARCH_INPUT)
    

    def enter_search_keyword(self,keyword):
        # 검색창에 검색 키워드 입력
        self.input_text(self.SEARCH_INPUT,keyword)
    
    def execute_search(self):
        # 검색 실행
        element = self.find_element(self.SEARCH_INPUT)
        element.send_keys(Keys.RETURN)

    



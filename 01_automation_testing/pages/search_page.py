# /pages/search_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

from selenium.webdriver.common.keys import Keys

# URL 파싱 관련
from urllib.parse import urlparse,parse_qs



"""
원티드는 검색 모달창하고 검색 결과 페이지가 두 개로 나뉘어짐
총 2개의 클래스를 생성해서 구현
"""

class SearchModal(BasePage):
    
    # locators
    SEARCH_ICON = (By.CSS_SELECTOR,"button[data-gnb-kind='search']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "[role='presentation'] input[type='search']")
    RECENT_SEARCH_KEYWORD = (By.CSS_SELECTOR,"ul[class*='RecentSearchList'] li a") 
    # class명에 RecentSearchList를 포함하는 ul의 li의 a
    TOAST_MESSAGE = (By.CSS_SELECTOR,"[role='alert']")
    AUTOCOMPLETE_SUGGESTION = (By.CSS_SELECTOR,"ul[class*='RelatedSearchResults_RecentSearchList'] li a")


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
        
        
    '''
    최근검색어
    '''
    def get_recent_searches(self):
        # 최근 검색어 리스트 추출
        text_list = []
        recent_search_elements = self.find_elements(self.RECENT_SEARCH_KEYWORD)
        for element in recent_search_elements:
            text_list.append(element.text)
        
        return text_list
    
    def is_recent_search_visible(self,keyword):
        # 검색어 리스트에 사용자가 검색한 keyword가 있는지 확인
        return keyword in self.get_recent_searches()
    
    '''
    자동완성
    '''
    def is_autocomplete_visible(self):
        # 자동완성 요소가 보이는지 확인
        return self.is_element_visible(self.AUTOCOMPLETE_SUGGESTION)
    
    def get_autocomplete_suggestions(self):
        # 자동완성 리스트 추출
        text_list = []
        suggestion_elements = self.find_elements(self.AUTOCOMPLETE_SUGGESTION)
        for element in suggestion_elements:
            text_list.append(element.text)
            
        return text_list
        
        
    '''
    Toast UI
    '''
    def is_toast_visible(self):
        # Toast UI가 보이는지 확인
        return self.is_element_visible(self.TOAST_MESSAGE)
    
    def get_toast_message(self):
        # Toast UI 메시지 추출
        return self.get_text(self.TOAST_MESSAGE)
        
        
class SearchResultsPage(BasePage):
    # locators
    TAB_PANEL = (By.CSS_SELECTOR,"[role='tabpanel']")
    NO_RESULT_MESSAGE = (By.XPATH,"//*[contains(text(),'검색 결과가 없어요')]")
    def __init__(self,driver):
        super().__init__(driver)
    
    def is_loaded(self):
        # 교차 검증을 통해 페이지 로드 확인
        return ("/search?" in self.get_current_url()
                and
                self.is_element_visible(self.TAB_PANEL))
    
    def get_search_query(self):
        # URL에서 검색어 추출
        current_url = self.get_current_url()
        parsed_url = urlparse(current_url)
        query_params = parse_qs(parsed_url.query) # 디코딩
        return query_params.get("query",[None])[0]
        
    



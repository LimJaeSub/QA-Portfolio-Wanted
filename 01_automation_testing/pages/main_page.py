# /pages/main_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from config.config import Config


class MainPage(BasePage):
    # locators
    AI_SEARCH_BUTTON = (By.CSS_SELECTOR, "button[wds-component='text-button'][data-color='primary']")
    PAGE_TITLE = "원티드 - 일하는 사람들의 모든 가능성"

    """
    shortcut menu datakind

    position : 채용공고
    positionAgent : 원티드에이전트
    resumeList : 이력서 관리
    scrapCareer : 커리어조회
    applicationStatus : 지원현황
    replyMatchup : 지원면접제안
    aiinterview : 면접 코칭받기
    bookmark : 북마크
    salary : 직군별 연봉
    wpoint : 원티드포인트
    """

    def __init__(self,driver):
        super().__init__(driver) 
        # basepage의 __init__ 실행
        # basepage의 self.driver = driver 실행
        
        
    # main page로 이동
    def navigate(self):
        self.navigate_to_url(Config.BASE_URL)
        
    
    # shortcut menu 클릭
    def click_shortcut_menu(self,data_kind):
        locator = (By.CSS_SELECTOR, f"[data-kind='{data_kind}']")
        self.click(locator)
        # main_page가 base_page의 click을 상속받아서 base_page의 click을 실행시킴
    
    # main page가 로드 되었는지 확인 
    def is_loaded(self):
        """main page가 로드 되었는지 확인"""
        return (self.get_page_title() == self.PAGE_TITLE and 
                "wanted.co.kr" in self.get_current_url())
    
    # # AI 검색어 입력 후 엔터
    # def search_ai(self, keyword):
    #     self.input_text(self.AI_SEARCH_INPUT, keyword) # AI 검색 input에 키워드 입력
    #     element = self.find_element(self.AI_SEARCH_INPUT) # AI 검색 input 요소를 찾은 후~
    #     element.send_keys(Keys.ENTER) # 엔터 입력

    def click_ai_agent_button(self):
        self.click(self.AI_SEARCH_BUTTON)
    


        
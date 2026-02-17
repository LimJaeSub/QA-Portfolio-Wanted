# /pages/main_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from config.config import Config
import time


class MainPage(BasePage):
    # locators
    AI_SEARCH_BUTTON = (By.CSS_SELECTOR, "button[wds-component='text-button'][data-color='primary']")
    PAGE_TITLE = "원티드 - 일하는 사람들의 모든 가능성"

    # 슬라이더
    SLIDER_NEXT_BUTTON = (By.CSS_SELECTOR, "button[aria-label='다음']")
    SLIDER_PREV_BUTTON = (By.CSS_SELECTOR, "button[aria-label='이전']")
    
    #슬라이더 카드
    SLIDER_CARDS = (By.CSS_SELECTOR, "li[class*='AttentionalJobCard']")

    # 카드 내부 요소
    CARD_TITLE = (By.CSS_SELECTOR, "span[class*='JobCard__body__position']")
    CARD_COMPANY = (By.CSS_SELECTOR, "span[class*='CompanyNameWithLocationPeriod_company']")
    CARD_LOCATION = (By.CSS_SELECTOR, "span[class*='CompanyNameWithLocationPeriod'][class*='location']")    

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


    # === 슬라이더 관련 메서드 ===
    def get_visible_card_titles(self):
        """
        실제로 화면에 보이는 슬라이드 카드 제목 가져오기
        viewport 기반 체크
        """
        cards = self.find_elements(self.SLIDER_CARDS)
        visible_titles = []
        
        for card in cards:
            try:
                # JavaScript로 viewport 안에 있는지 확인
                is_in_viewport = self.driver.execute_script("""
                    var elem = arguments[0];
                    var rect = elem.getBoundingClientRect();
                    var windowHeight = window.innerHeight || document.documentElement.clientHeight;
                    var windowWidth = window.innerWidth || document.documentElement.clientWidth;
                    
                    // 카드가 화면 안에 있는지 확인
                    var vertInView = (rect.top >= 0) && (rect.bottom <= windowHeight);
                    var horInView = (rect.left >= 0) && (rect.right <= windowWidth);
                    
                    return (vertInView && horInView && rect.width > 0 && rect.height > 0);
                """, card)
                
                if is_in_viewport:
                    title_elem = card.find_element(*self.CARD_TITLE)
                    title_text = title_elem.text.strip()
                    if title_text:
                        visible_titles.append(title_text)
                        
            except Exception as e:
                pass
        
        print(f"📊 Viewport 내 카드: {len(visible_titles)}개")
        return visible_titles[:4]  # 최대 4개만 반환
    
    def click_slider_right(self):
        """슬라이더 오른쪽(다음) 버튼 클릭"""
        self.click(self.SLIDER_NEXT_BUTTON)
        time.sleep(5)  # 애니메이션 대기
    
    
    def click_slider_left(self):
        """슬라이더 왼쪽(이전) 버튼 클릭"""
        self.click(self.SLIDER_PREV_BUTTON)
        time.sleep(5)  # 애니메이션 대기 

    def is_slider_right_enabled(self):
        """오른쪽 버튼이 활성화되어 있는지 확인"""
        try:
            button = self.find_element(self.SLIDER_NEXT_BUTTON)
            is_disabled = (
                button.get_attribute("disabled") is not None or
                button.get_attribute("aria-disabled") == "true"
            )
            return not is_disabled
        except:
            return False
    


        
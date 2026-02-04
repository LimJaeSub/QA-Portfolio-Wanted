from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class JobListPage(BasePage):
    #URL
    URL_PATH = "/wdlist"

    # 최상단 필터 버튼
    JOB_GROUP_BUTTON = (By.XPATH, "//button[contains(text(), '직군 전체')]")
    CAREER_GROUP_BUTTON = (By.XPATH,"//button[contains(text(),'경력 전체')]")

    # 직군 필터 목록
    CATEGORY_DEV = (By.XPATH, "//div[contains(text(), '개발')]")

    # 직군 > 상세 필터 목록
    JOB_QA = (By.XPATH, "//button[contains(text(), 'QA 테스트 엔지니어')]")

    # 버튼
    APPLY_BUTTON = (By.XPATH, "//button[contains(text(), '적용')]")
    RESET_BUTTON = (By.XPATH, "//button[contains(text(), '초기화')]")

    # 결과 카드
    JOB_CARDS = (By.CSS_SELECTOR, "li.Card_Card__aaatv")


    def __init__(self, driver):
        super().__init__(driver)
    
    
    def is_loaded(self):
        # 페이지 로드 확인
        return self.URL_PATH in self.get_current_url()
    
    def click_job_group_button(self):
        # 직군 직무 버튼 클릭
        self.click(self.JOB_GROUP_BUTTON)
        time.sleep(1)   

     
    # 필터 선택
    def select_category(self, category_name):
        """
        왼쪽 대분류 카테고리 선택
        예: "개발", "경영·비즈니스", "마케팅·광고"
        """
        locator = (By.XPATH, f"//div[contains(text(), '{category_name}')]")
        self.click(locator)
        time.sleep(1)
    
    
    def select_job(self, job_name):
        """
        오른쪽 세부 직무 선택 (스크롤 포함)
        예: "QA 테스트 엔지니어", "서버 개발자"
        """
        locator = (By.XPATH, f"//button[contains(text(), '{job_name}')]")
        
        # 스크롤이 필요할 수 있음
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)
        
        self.click(locator)
        time.sleep(1)

    # 필터 적용/초기화
    
    def apply_filter(self):
        """적용 버튼 클릭"""
        self.click(self.APPLY_BUTTON)
        time.sleep(2)
    
    
    def reset_filter(self):
        """초기화 버튼 클릭"""
        self.click(self.RESET_BUTTON)
        time.sleep(2)

    # 결과 검증
    def get_job_cards_count(self):
        """채용 공고 결과 개수 반환"""
        cards = self.find_elements(self.JOB_CARDS)
        return len(cards)

    def keyword


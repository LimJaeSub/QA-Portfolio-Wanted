from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class JobListPage(BasePage):
    # URL
    URL_PATH = "/wdlist"

    # 최상단 필터 버튼
    JOB_GROUP_BUTTON = (By.CSS_SELECTOR, "button[data-filter-name='jobCategory,jobRole']")

    # 버튼
    APPLY_BUTTON = (By.XPATH, "//button[contains(text(), '적용')]")
    RESET_BUTTON = (By.XPATH, "//button[contains(text(), '초기화')]")

    # 결과 카드
    JOB_CARDS = (By.CSS_SELECTOR, "li.Card_Card__aaatv")


    def __init__(self, driver):
        super().__init__(driver)
    
    
    def is_loaded(self):
        """페이지 로드 확인"""
        return self.URL_PATH in self.get_current_url()
    
    
    # ===== 직군 필터 =====
    
    def click_job_group_button(self):
        """직군·직무 버튼 클릭"""
        self.click(self.JOB_GROUP_BUTTON)
        time.sleep(1)
    
    
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
    
    
    # ===== 필터 적용/초기화 =====
    
    def apply_filter(self):
        """적용 버튼 클릭"""
        self.click(self.APPLY_BUTTON)
        time.sleep(2)
    
    
    def reset_filter(self):
        """초기화 버튼 클릭"""
        self.click(self.RESET_BUTTON)
        time.sleep(2)
    
    
    # ===== 결과 검증 =====
    
    def get_job_cards_count(self):
        """채용 공고 결과 개수 반환"""
        cards = self.find_elements(self.JOB_CARDS)
        return len(cards)
    
    
    def keyword_in_job_cards(self, keyword):
        """5개 이상 채용 공고 카드에 특정 키워드가 포함되어 있는지 확인"""
        cards = self.find_elements(self.JOB_CARDS)
        count = 0
        
        for card in cards:
            if keyword.lower() in card.text.lower():
                count += 1
        
        print(f"'{keyword}' 포함 카드: {count}/{len(cards)}개")
        return count >= 5
    
    
    def is_filter_reset_in_modal_job(self):
        """필터 모달 내 직군 초기화 상태 확인"""
        try:
            left_panel = self.find_element(
                (By.XPATH, "//div[contains(text(), '직군 전체')]")
            )
            
            right_message = self.find_element(
                (By.XPATH, "//div[contains(text(), '직군을 선택하면')]")
            )
            
            return left_panel is not None and right_message is not None
            
        except:
            return False
    
    
    def is_filter_reset_job(self):
        """직군 필터가 초기화 상태인지 확인"""
        job_group_text = self.get_text(self.JOB_GROUP_BUTTON)
        return "직군 전체" in job_group_text
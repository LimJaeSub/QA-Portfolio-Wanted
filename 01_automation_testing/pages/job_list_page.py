# pages/job_list_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class JobListPage(BasePage):
    # URL
    URL_PATH = "/wdlist"

    # 최상단 필터 버튼
    JOB_GROUP_BUTTON = (By.CSS_SELECTOR, "button[data-filter-name='jobCategory,jobRole']")
    LOCATION_BUTTON = (By.CSS_SELECTOR, "button[data-filter-name='region']")
    
    # 버튼
    APPLY_BUTTON = (By.XPATH, "//button[contains(., '적용')]")
    RESET_BUTTON = (By.XPATH, "//button[contains(., '초기화')]")

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
        locator = (By.XPATH, f"//button[contains(., '{category_name}')]")
        self.click(locator)
        time.sleep(1)
    
    
    def select_job(self, job_name):
        """
        오른쪽 세부 직무 선택 (스크롤 포함)
        예: "QA 테스트 엔지니어", "서버 개발자"
        """
        locator = (By.XPATH, f"//button[contains(., '{job_name}')]") 
    
        # 오른쪽 직무 목록 ul 찾기
        uls = self.find_elements(
            (By.CSS_SELECTOR, "div[class*='CategorySelectModal'] ul")
        )
        
        job_list_container = uls[1] # 두 번째 ul이 오른쪽 직무 목록임
        
        
        # 반복 스크롤 하면서 요소 찾기
        for i in range(10):
            try:
                element = self.driver.find_element(*locator)
                if element.is_displayed():
                    self.click(locator)
                    time.sleep(1)
                    return
            except:
                pass
            
            # 스크롤 다운
            self.driver.execute_script(
                "arguments[0].scrollBy(0, 200);", job_list_container
            )
            time.sleep(0.3)
            
        raise Exception(f"직무 '{job_name}' 요소를 찾을 수 없음")
                
    # === 지역 필터 ===
    def click_location_button(self):
        """지역 버튼 클릭"""
        self.click(self.LOCATION_BUTTON)
        time.sleep(1)
        
    def select_location(self, country_name, location_name, district_name):
        """
        국가 > 지역 > 세부지역 선택 (스크롤 포함)
        예: "한국", "서울", "관악구"
        """
        
        # 1. 국가 선택
        country_dropdown = (By.XPATH, "//h6[contains(., '국가')]/following-sibling::div//button")
        self.click(country_dropdown)
        time.sleep(0.5)
        
        select_country = (By.XPATH, f"//li[contains(., '{country_name}')]")
        self.click(select_country)
        time.sleep(1)
        
        # 2. 왼쪽 지역 선택 (스크롤 포함)
        location_locator = (By.XPATH, f"//div[contains(@class, 'Locations')]//button[contains(., '{location_name}')]")
        
        location_containers = self.find_elements((By.CSS_SELECTOR, "div[class*='Locations'] ul"))
        
        if location_containers:
            location_ul = location_containers[0]
            
            for i in range(10):
                try:
                    element = self.driver.find_element(*location_locator)
                    if element.is_displayed():
                        element.click()
                        time.sleep(1)
                        break
                except:
                    pass
                
                self.driver.execute_script("arguments[0].scrollBy(0, 200);", location_ul)
                time.sleep(0.1)
        else:
            self.click(location_locator)
            time.sleep(1)
        
        # 3. 오른쪽 세부지역 선택 (스크롤 포함)
        district_locator = (By.XPATH, f"//div[contains(@class, 'Districts')]//button[contains(., '{district_name}')]")
        
        district_containers = self.find_elements((By.CSS_SELECTOR, "div[class*='Districts'] ul"))
        
        if district_containers:
            district_ul = district_containers[0]
            
            for i in range(10):
                try:
                    element = self.driver.find_element(*district_locator)
                    if element.is_displayed():
                        element.click() 
                        time.sleep(0.5)
                        break
                except:
                    pass
                
                self.driver.execute_script("arguments[0].scrollBy(0, 200);", district_ul)
                time.sleep(0.1)
        else:
            self.click(district_locator)
            time.sleep(0.5)
        
        

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
    
    # --- 상세 페이지 이동 확인 ---
    def get_first_card_position_id(self):
        """
        첫 번째 채용 카드의 position-id 가져오기
        """
        cards = self.find_elements(self.JOB_CARDS)
        
        if cards:
            first_card = cards[0]
            try:
                # 북마크 버튼의 data-position-id 사용
                bookmark_btn = first_card.find_element(
                    By.CSS_SELECTOR, 
                    "button[data-attribute-id='position__bookmark__click']"
                )
                position_id = bookmark_btn.get_attribute("data-position-id")
                return position_id
            except:
                pass
        
        return None
    
    def go_to_first_job_detail(self):
        """첫 번째 채용 공고 상세 페이지로 이동"""
        cards = self.find_elements(self.JOB_CARDS)
        
        if cards:
            first_card = cards[0]
            first_card.click()
            time.sleep(2)

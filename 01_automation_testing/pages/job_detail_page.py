from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class JobDetailPage(BasePage):
    # URL 패턴
    URL_PATH = "/wd/"

    # Locators
    BOOKMARK_BUTTON = (By.CSS_SELECTOR, "button[data-attribute-id='position__bookmark__click']")

    JOB_DESCRIPTION_SECTION = (By.CSS_SELECTOR, "article.JobDescription_JobDescription__s2Keo")
    JOB_DESCRIPTION_H2 = (By.XPATH, "//article[contains(@class, 'JobDescription')]//h2[contains(., '포지션 상세')]")
    JOB_DESCRIPTION_H3 = (By.XPATH, "//article[contains(@class, 'JobDescription')]//h3")
    JOB_DESCRIPTION_SPANS = (By.XPATH, "//article[contains(@class, 'JobDescription')]//span")

    MAP_SECTION = (By.CSS_SELECTOR, "article[class*='JobWorkPlace']")  # ✅
    MAP_H2 = (By.XPATH, "//article[contains(@class, 'JobWorkPlace')]//h2[contains(., '근무지역')]")
    MAP_COMPONENT = (By.CSS_SELECTOR, "div[class*='NaverMap']")  # ✅

    def __init__(self, driver):
        super().__init__(driver)

    def is_loaded(self):
        """페이지 로드 확인"""
        return self.URL_PATH in self.get_current_url()
    
    def get_position_id_from_url(self):
        """URL에서 position ID 추출"""
        current_url = self.get_current_url()
        
        if "/wd/" in current_url:
            position_id = current_url.split("/wd/")[-1].split("?")[0]
            return position_id
        
        return None
    
    def scroll_and_find(self, locator, max_scrolls=20):
        """
        페이지를 스크롤하면서 요소 찾기
        찾으면 True, 못 찾으면 False
        """
        for i in range(max_scrolls):
            try:  # ← 추가!
                element = self.driver.find_element(*locator)
                if element.is_displayed():
                    # 요소를 중앙으로 스크롤
                    self.driver.execute_script(
                        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                        element
                    )
                    time.sleep(0.5)
                    return True
            except:  # ← 추가!
                pass  # 못 찾으면 계속
            
            # 페이지 아래로 스크롤 (화면 높이만큼)
            self.driver.execute_script("window.scrollBy(0, window.innerHeight);")
            time.sleep(0.3)
        
        return False
    
    # === 북마크 ===
    def is_bookmarked_visible(self):
        """북마크 버튼이 보이는지 확인"""
        return self.is_element_visible(self.BOOKMARK_BUTTON)
    
    # === 포지션 상세 ===
    def verify_job_description_content(self):
        """
        포지션 상세 전체 검증 (스크롤 포함)
        - h2 태그 존재
        - h3 태그 존재
        - 내용(span) 존재
        """
        # 섹션까지 스크롤
        if not self.scroll_and_find(self.JOB_DESCRIPTION_SECTION):
            print("포지션 상세 섹션을 찾을 수 없음")
            return False
        
        # h2 확인
        has_h2 = self.is_element_present(self.JOB_DESCRIPTION_H2)
        
        # h3 확인
        h3_elements = self.find_elements(self.JOB_DESCRIPTION_H3)
        has_h3 = len(h3_elements) > 0
        
        # span 내용 확인
        span_elements = self.find_elements(self.JOB_DESCRIPTION_SPANS)
        has_content = False
        if len(span_elements) > 0:
            for span in span_elements:
                if span.text.strip():
                    has_content = True
                    break
        
        print(f"포지션 상세 - h2: {has_h2}, h3: {has_h3}, 내용: {has_content}")
        
        return has_h2 and has_h3 and has_content
    
    # === 지도 ===
    def is_map_visible(self):
        """지도 섹션 존재 확인 (스크롤 포함)"""
        if not self.scroll_and_find(self.MAP_SECTION):
            return False
        return self.is_element_visible(self.MAP_SECTION)
    
    def has_map_h2(self):
        """지도 h2 태그(근무지역) 확인"""
        self.scroll_and_find(self.MAP_SECTION)
        return self.is_element_present(self.MAP_H2)
    
    def has_map_component(self):
        """네이버 지도 컴포넌트 확인"""
        self.scroll_and_find(self.MAP_SECTION)
        return self.is_element_visible(self.MAP_COMPONENT)
    
    def verify_map_section(self):
        """
        지도 전체 검증 (스크롤 포함)
        - h2 태그 존재
        - 지도 컴포넌트 존재
        """
        # 지도 섹션까지 스크롤
        if not self.scroll_and_find(self.MAP_SECTION):
            print("지도 섹션을 찾을 수 없음")
            return False
        
        has_h2 = self.is_element_present(self.MAP_H2)
        has_map = self.is_element_visible(self.MAP_COMPONENT)
        
        print(f"지도 - h2: {has_h2}, 지도 컴포넌트: {has_map}")
        
        return has_h2 and has_map
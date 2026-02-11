# pages/job_detail_page.py

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
    JOB_DESCRIPTION_SPANS = (By.XPATH, "//article[contains(@class, 'JobDescription')]//h3//following-sibling::div//span")

    MAP_SECTION = (By.CSS_SELECTOR, "article.JobWorkPlace_JobWorkPlace__xPIGe")
    MAP_H2 = (By.XPATH, "//article[contains(@class, 'JobWorkPlace')]//h2[contains(., '근무지역')]")
    MAP_COMPONENT = (By.CSS_SELECTOR, "div.NaverMap_NaverMap__tpI6f")


    def __init__(self, driver):
        super().__init__(driver)

    def is_loaded(self):
        """페이지 로드 확인"""
        return self.URL_PATH in self.get_current_url()
    
    # === 북마크 ===
    def is_bookmarked_visible(self):
        """북마크 버튼이 보이는지 확인"""
        return self.is_element_visible(self.BOOKMARK_BUTTON)
    
    # === 포지션 상세 ===
    def is_job_description_section_visible(self):
        """포지션 상세 섹션이 보이는지 확인"""
        return self.is_element_visible(self.JOB_DESCRIPTION_SECTION)
    
    def has_job_description_h2(self):
        """포지션 상세 h2 태그 확인"""
        return self.is_element_present(self.JOB_DESCRIPTION_H2)
    
    
    def has_job_description_h3(self):
        """포지션 상세 h3 태그 확인 (주요업무, 자격요건, 우대사항 등)"""
        h3_elements = self.find_elements(self.JOB_DESCRIPTION_H3)
        return len(h3_elements) > 0   
    
    def has_job_description_spans(self):
        """포지션 상세 설명에 span 태그가 포함되어 있는지 확인"""
        span_elements = self.find_elements(self.JOB_DESCRIPTION_SPANS)
        
        # span 태그가 있고, 내용이 있는지 확인
        if len(span_elements) > 0:
            for span in span_elements:
                if span.text.strip():
                    return True
        return False
    
    def verify_job_description_content(self):
        """포지션 상세 섹션의 h2, h3, span 태그 내용 확인"""
        return (self.has_job_description_h2() and 
                self.has_job_description_h3() and 
                self.has_job_description_spans())
    
    # === 지도 ===
    def is_map_visible(self):
        """지도 섹션 존재 확인"""
        return self.is_element_visible(self.MAP_SECTION)
    
    
    def has_map_h2(self):
        """지도 h2 태그(근무지역) 확인"""
        return self.is_element_present(self.MAP_H2)
    
    
    def has_map_component(self):
        """네이버 지도 컴포넌트 확인"""
        return self.is_element_visible(self.MAP_COMPONENT)
    
    
    def verify_map_section(self):
        """
        지도 전체 검증
        - h2 태그 존재
        - 지도 컴포넌트 존재
        """
        return self.has_map_h2() and self.has_map_component()    
    

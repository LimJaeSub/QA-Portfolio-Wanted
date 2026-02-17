# 01_automation_testing/pages/base_page.py
## 모든 Page Object의 공통 기능을 정의함

import time
# page 대기 관련
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 예외 처리
from selenium.common.exceptions import TimeoutException

from config.config import Config

class BasePage:
    # 모든 페이지의 기본 기능 클래스
    
    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        # timeout 조절이 필요하지 않은 것들은 self.wait 사용
    
    def find_element(self, locator,timeout=None):
        #요소 찾기
        wait_time = timeout if timeout else Config.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver,wait_time)
        return wait.until(EC.presence_of_element_located(locator))
    
        
        """
        *locator를 쓰는 이유?
        기존 driver.find_element는 2개의 인자를 받는다
        ex) driver.find_element(By.CSS_SELECTOR,"#query")

        BasePage 클래스에서는 어떤 인자가 올 지 몰라서 *locator로 압축하여 전달한다.
        """
    
    def find_elements(self, locator,timeout=None):
        # 여러 요소 찾기
        try:
            wait_time = timeout if timeout else Config.EXPLICIT_WAIT
            wait = WebDriverWait(self.driver,wait_time)
            return wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            return []
    
    def click(self, locator):
        # 요소 클릭
        element = self.wait.until(EC.element_to_be_clickable(locator)) #요소가 클릭 가능할때 까지 대기
        element.click()

        """
        여기선 왜 locator를 사용?
        EC.element_to_be_clickable은 하나의 인자만 받는다.
        ex) EC.element_to_be_clickable((By.CSS_SELECTOR, "input.search"))
        """
    
    def input_text(self, locator, text):
        # 텍스트 입력 
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        # 요소의 텍스트 추출
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
    
    def is_element_visible(self, locator, timeout=None):
        #요소 보이는지 확인
        try:
            wait_time = timeout if timeout else Config.EXPLICIT_WAIT # 대기 시간 설정
            wait = WebDriverWait(self.driver, wait_time)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException: 
            return False
    
    def is_element_present(self, locator):
        # 요소 DOM에 존재하는지 확인
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def get_current_url(self):
        # 현재 URL
        return self.driver.current_url
    
    def navigate_to_url(self,url):
        # url 이동
        self.driver.get(url)
    
    def get_page_title(self):
        # 현재 타이틀
        return self.driver.title
    
    def set_mobile_viewport(self):
        # 모바일 뷰포트 전환(375x667)
        self.driver.set_window_size(375, 667)
        time.sleep(1)
    
    def set_desktop_viewport(self):
        # 데스크탑 뷰포트 전환(1920x1080)
        self.driver.set_window_size(1920, 1080)
        time.sleep(1)
    
    def get_window_size(self):
        # 현재 창 크기 반환
        size = self.driver.get_window_size()
        return size['width'], size['height']
    
    



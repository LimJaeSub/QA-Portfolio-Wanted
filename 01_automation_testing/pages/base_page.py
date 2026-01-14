# 01_automation_testing/pages/base_page.py
## 모든 Page Object의 공통 기능을 정의함


# page 대기 관련
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_condirions as EC

# 예외 처리
from selenium.common.exceptions import TimeoutException

from config.config import Config

class BasePage:
    # 모든 페이지의 기본 클래스

    def __init__(self,driver):

        # 드라이버 및 대기 시간 정의
        self.driver = driver
        self.wait = WebDriverWait(driver,Config.EXPLICIT_WAIT)
    
    def find_element(self,locator):
        



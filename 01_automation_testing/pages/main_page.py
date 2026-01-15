# /pages/main_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    # locators
    AI_SEARCH_INPUT = (By.CSS_SELECTOR,"[data-role='test-field-wrapper] input")

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

    def click_shortcut_menu(self,data_kind):
        locator = (By.CSS_SELECTOR, f"[data-kind='{data_kind}']")
        self.click(locator)
        # main_page가 base_page의 click을 상속받아서 base_page의 click을 실행시킴



        
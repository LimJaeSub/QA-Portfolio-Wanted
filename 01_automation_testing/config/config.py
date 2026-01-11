# 02-automation-testing/config/config.py
# 값 설정 파일

import os
from pathlib import Path # Path 모듈 임포트
from dotenv import load_dotenv # .env 파일 로드용 모듈 임포트

env_path = Path(__file__).parent / ".env" # .env 파일 경로(위치)
load_dotenv(dotenv_path=env_path) # .env 파일 로드


class Config:
    
    # 폴더 경로
    BASE_DIR = Path(__file__).parent.parent # 01_automation_testing 폴더 경로
    REPORTS_DIR = BASE_DIR / "reports"  # 리포트 저장 폴더 경로
    
    
    # 환경 설정
    BASE_URL = os.getenv("BASE_URL","https://www.wanted.co.kr/")
    BROWSER = os.getenv("BROWSER","chrome").lower()
    HEADLESS = os.getenv("HEADLESS","false").lower() == "true"
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "20"))
    
    # 테스트 계정 (향후 로그인 테스트용)
    TEST_EMAIL = os.getenv("TEST_EMAIL")
    TEST_PASSWORD = os.getenv("TEST_PASSWORD")
    
    
    # 
    @staticmethod
    def get_chrome_options():
        from selenium.webdriver.chrome.options import Options
        
        options = Options()
        
        # 봇 탐지 우회 설정
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        
        # 기본 옵션
        if Config.HEADLESS:
            # 헤드리스 모드(창 없이 실행)
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
        else:
            # 일반 모드(창 있음)
            options.add_argument("--start-maximized")
            
        # 알림 비활성화
        options.add_argument("--disable-notifications")
        
        # 팝업 차단 비활성화
        options.add_argument("--disable-popup-blocking")
        
        # GPU 비활성화 (안정성 향상)
        options.add_argument("--disable-gpu")
        
        return options
            
            
        

# 02-automation-testing/test_config.py

"""
Config 테스트 스크립트
"""

from config import Config


def test_basic_config():
    """기본 설정 확인"""
    print("\n" + "=" * 60)
    print("기본 설정 테스트")
    print("=" * 60)
    
    print(f"\n[경로]")
    print(f"  BASE_DIR        : {Config.BASE_DIR}")
    #print(f"  REPORTS_DIR     : {Config.REPORTS_DIR}")
    #print(f"  SCREENSHOTS_DIR : {Config.SCREENSHOTS_DIR}")
    
    print(f"\n[환경]")
    print(f"  BASE_URL        : {Config.BASE_URL}")
    print(f"  BROWSER         : {Config.BROWSER}")
    print(f"  HEADLESS        : {Config.HEADLESS}")
    
    print(f"\n[대기 시간]")
    print(f"  IMPLICIT_WAIT   : {Config.IMPLICIT_WAIT}초")
    print(f"  EXPLICIT_WAIT   : {Config.EXPLICIT_WAIT}초")
    
    print(f"\n[테스트 계정]")
    print(f"  EMAIL           : {'설정됨' if Config.TEST_EMAIL else '없음'}")
    print(f"  PASSWORD        : {'설정됨' if Config.TEST_PASSWORD else '없음'}")
    
    print("\n✅ 기본 설정 확인 완료")


def test_chrome_options():
    """Chrome 옵션 생성 테스트"""
    print("\n" + "=" * 60)
    print("Chrome 옵션 테스트")
    print("=" * 60)
    
    try:
        options = Config.get_chrome_options()
        print("\n✅ Chrome 옵션 생성 성공")
        print(f"   타입: {type(options)}")
    except Exception as e:
        print(f"\n❌ Chrome 옵션 생성 실패: {e}")


def test_driver_creation():
    """WebDriver 생성 및 스텔스 모드 테스트"""
    print("\n" + "=" * 60)
    print("WebDriver 생성 테스트")
    print("=" * 60)
    
    response = input("\nWebDriver를 실제로 생성하시겠습니까? (y/n): ")
    if response.lower() != 'y':
        print("건너뛰기")
        return
    
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        
        print("\n1. Chrome 옵션 생성...")
        options = Config.get_chrome_options()
        
        print("2. ChromeDriver 설치...")
        service = Service(ChromeDriverManager().install())
        
        print("3. WebDriver 생성...")
        driver = webdriver.Chrome(service=service, options=options)
        
        print("4. 스텔스 모드 적용...")
        Config.setup_driver_stealth(driver)
        
        print("5. 원티드 접속...")
        driver.get(Config.BASE_URL)
        
        print("\n6. navigator.webdriver 확인...")
        webdriver_value = driver.execute_script("return navigator.webdriver")
        print(f"   navigator.webdriver: {webdriver_value}")
        
        if webdriver_value is None:
            print("   ✅ 봇 탐지 방지 성공!")
        else:
            print("   ⚠️ 봇으로 감지될 수 있음")
        
        input("\n확인 후 엔터를 누르세요...")
        
        print("\n7. WebDriver 종료...")
        driver.quit()
        print("   ✅ 종료 완료")
        
    except Exception as e:
        print(f"\n❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()


# def test_validation():
#     """설정 검증 테스트"""
#     print("\n" + "=" * 60)
#     print("설정 검증 테스트")
#     print("=" * 60)
    
#     try:
#         Config.validate()
#         print("\n✅ 모든 검증 통과")  
#     except ValueError as e:
#         print(f"\n❌ 검증 실패:\n{e}")


def main():
    """전체 테스트 실행"""
    print("\n" + "=" * 60)
    print("CONFIG.PY 테스트")
    print("=" * 60)
    
    # 1. 기본 설정
    test_basic_config()
    
    # 2. Chrome 옵션
    test_chrome_options()
    
    # # 3. 검증
    # test_validation()
    
    # 4. WebDriver 생성 (선택)
    test_driver_creation()
    
    print("\n" + "=" * 60)
    print("✅ 모든 테스트 완료!")
    print("=" * 60)


if __name__ == "__main__":
    main()
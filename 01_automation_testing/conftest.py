# 02-automation-testing/conftest.py

# TODO: import 작성
# 필요한 것들:
# - pytest
# - selenium webdriver
# - Config 클래스


# TODO: browser fixture 작성
# 해야할 일:
# 1. Chrome 옵션 가져오기 (Config에서)
# 2. 브라우저 생성
# 3. 설정 적용 (대기시간, 최대화)
# 4. 테스트에 전달 (yield)
# 5. 종료 (quit)



# import 작성
import pytest
from selenium import webdriver
from config.config import Config


# pytest작성
@pytest.fixture(scope="function")
def browser():
    # Setup : 브라우저 생성
    options = Config.get_chrome_options() # config에서 크롬 옵션 가져오기
    driver = webdriver.Chrome(options=options) # 가져온 option으로 driver 생성
    driver.implicitly_wait(Config.IMPLICIT_WAIT) # 대기 시간 생성
    driver.maximize_window() # 화면 최대화

    print(f"Setup 완료")

    yield driver # driver 전달

    # 브라우저 종료
    print(f"브라우저 종료")
    driver.quit()
    print(f"종료 완료")

@pytest.fixture(scope="session")
def base_url():
    # 세션 한번만 생성하는 baseurl
    return Config.BASE_URL
import time
import pytest
from pages.search_page import SearchModal, SearchResultsPage

def test_result_page(browser,base_url):
    """검색 전체 플로우 : TC_001"""

    browser.get(base_url)
    time.sleep(2)

    # 검색 모달 열기
    modal = SearchModal(browser)
    modal.open_modal()
    time.sleep(2)

    # 검색어 입력 및 실행
    keyword = "QA"
    modal.enter_search_keyword(keyword)
    modal.execute_search()
    time.sleep(3)

    # 결과 페이지로 전환 & 로드 확인
    result_page = SearchResultsPage(browser)
    time.sleep(1)
    assert result_page.is_loaded()

    # URL에 검색어 포함 확인
    search_query = result_page.get_search_query()
    assert search_query==keyword

    print("✅ TC_001 통과: 검색 성공")


def test_result_count_matches(browser,base_url):
    # 타이틀의 갯수와 실제 갯수 비교 : TC_008
    
    browser.get(base_url)
    time.sleep(2)

    # 검색 모달 열기
    modal = SearchModal(browser)
    modal.open_modal()
    time.sleep(2)

    # 검색어 입력 및 실행
    keyword = "백엔드"
    modal.enter_search_keyword(keyword)
    modal.execute_search()
    time.sleep(3)

    # 결과 페이지로 전환 & 로드 확인
    result_page = SearchResultsPage(browser)
    time.sleep(1)
    assert result_page.is_loaded()

    ## 디폴트가 전체<<라서 탭 하나 클릭해야함 !
    result_page.click_tab("회사")
    time.sleep(5)

    #현재 활성화 탭을 확인
    active_tab = result_page.now_tab()
    print(f"\n 현재 탭 : {active_tab}")

    
    # 타이틀에 표시된 결과 갯수
    result_count = result_page.get_result_count_from_title()
    print(f"\n 타이틀에 표시된 갯수 : {result_count}")

    # 무한 스크롤로 실제 갯수 확인
    print("무한 스크롤 시작")
    scroll_count = result_page.count_result()
    time.sleep(5)
    assert result_count == scroll_count, \
        f"개수 불일치! 타이틀: {result_count}, 실제: {scroll_count}"
    print("개수 비교 테스트 종료")
    
    print("✅ TC_008 통과: 타이틀의 갯수와 실제 갯수 일치 확인")


def test_no_results(browser,base_url):
    """결과 없는 검색어 : TC_002"""
    browser.get(base_url)
    time.sleep(2)

    # 검색 모달 열기
    modal = SearchModal(browser)
    modal.open_modal()
    time.sleep(2)

    keyword = "zxcvbnm12345"
    modal.enter_search_keyword(keyword)
    modal.execute_search()
    time.sleep(3)

    result_page = SearchResultsPage(browser)
    time.sleep(1)
    assert result_page.is_loaded()

    # 검색 결과 없는 표시 확인
    assert result_page.is_no_result_page()

    # 검색 결과 없는 메시지 확인
    message = result_page.get_no_result_message()
    assert "검색 결과가 없어요" in message

    print(f"\n검색어: {keyword}")
    print(f"메시지: {message}")
    print("✅ TC_002 통과: 결과 없는 값 검색 확인")
    
@pytest.mark.skip(reason="로그인 필요 (테스트 계정 생성 불가, 이미 가입한 명의로 재가입 불가능)")
def test_recent_searches(browser,base_url):
    # 최근검색어 테스트 : TC_006

    browser.get(base_url)
    time.sleep(2)

    # 검색 모달 열기
    modal = SearchModal(browser)
    modal.open_modal()
    time.sleep(2)

    # 새로운 검색어 입력 및 실행
    keyword = "프론트엔드"
    modal.enter_search_keyword(keyword)
    modal.execute_search()
    time.sleep(3)
    
    # 결과 페이지 확인
    result_page = SearchResultsPage(browser)
    assert result_page.is_loaded()

    # 결과 페이지에서 다시 검색 모달 열기
    modal2 = SearchModal(browser)
    modal2.open_modal()
    time.sleep(2)
    assert modal2.is_modal_visible()

    # 최근 검색어에 방금 검색한 키워드가 있는지 확인
    recent_searches = modal2.get_recent_searches()
    assert modal2.is_recent_search_visible(keyword), \
        f"최근 검색어에 {keyword}가 없음"
        
    print(f"\n최근 검색어 리스트: {recent_searches}")
    print("✅ TC_006 통과: 최근 검색어에 새 검색어 추가 확인")







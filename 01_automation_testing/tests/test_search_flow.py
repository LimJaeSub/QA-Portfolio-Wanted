import time
from pages.search_page import SearchModal, SearchResultsPage

def test_result_page(browser,base_url):
    # 검색 전체 플로우

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

    print(f"\n검색 성공! 키워드: {keyword}")




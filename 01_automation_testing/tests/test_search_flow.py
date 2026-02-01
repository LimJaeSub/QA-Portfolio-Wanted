import time
from pages.search_page import SearchModal, SearchResultsPage
"""
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


def test_result_count_matches(browser,base_url):
    # 타이틀의 갯수와 실제 갯수 비교
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

   
    
    # 디버깅: RESULT_COUNT 요소 찾기 시도
    # print("RESULT_COUNT 요소 찾는 중...")
    # try:
    #     elements = result_page.find_elements(result_page.RESULT_COUNT)
    #     print(f"찾은 요소 개수: {len(elements)}")
    
    #     if len(elements) > 0:
    #         print(f"첫 번째 요소 텍스트: {elements[0].text}")
    #         print(f"첫 번째 요소 visible: {elements[0].is_displayed()}")
    
    #     # 강제로 첫 번째 요소 사용
    #     if len(elements) > 0 and elements[0].is_displayed():
    #         result_count = int(elements[0].text)
    #     else:
    #         raise Exception("요소를 찾았지만 보이지 않음!")
        
    # except Exception as e:
    #     print(f"에러: {e}")
    #     # 페이지 소스 일부 출력
    #     print("페이지에 'TitleCount' 있나?", 'TitleCount' in browser.page_source)
    # raise

    # print(f"타이틀 개수: {result_count}")


    
    
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
"""

def test_no_results(browser,base_url):
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
    assert ""








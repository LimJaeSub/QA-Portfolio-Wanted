from pages.search_page import SearchModal # 테스트할 클래스
import time

def test_open_modal(browser,base_url):
    """모달 열리는 것 확인"""
    browser.get(base_url)

    time.sleep(2) #페이지 로딩 대기
    
    print("페이지 오픈 완료")

    modal = SearchModal(browser)
    modal.open_modal()

    time.sleep(2) #open_modal 대기
    
    print("검색모달 오픈 완료")

    assert modal.is_modal_visible()


def test_empty_enter_keyword(browser,base_url):
    # 공백 검색어 입력 테스트 : TC_003
    
    browser.get(base_url)
    time.sleep(2)

    # 검색 모달 오픈
    modal = SearchModal(browser)
    modal.open_modal()
    time.sleep(2)

    # 공백 검색어 입력
    modal.enter_search_keyword(" ")
    time.sleep(2)

    # 검색어 입력 후 검색 실행
    modal.execute_search()
    time.sleep(2)

    # toastUI 확인 
    assert modal.is_toast_visible()

    # toast UI message 확인
    message = modal.get_toast_message()
    assert "검색어를 입력해주세요" in message
    print("✅ TC_003 통과: 공백 검색어 입력 테스트 성공")

def test_autocomplete(browser,base_url):
    """자동완성 기능 확인"""

    browser.get(base_url)
    time.sleep(2)

    # 검색 모달 오픈
    modal = SearchModal(browser)
    modal.open_modal()
    time.sleep(2)

    # 검색 키워드 입력
    keyword = "QA"
    modal.enter_search_keyword(keyword)
    time.sleep(2)

    # 자동완성 요소 표시 확인
    assert modal.is_autocomplete_visible()

    # 자동완성 항목 가져오기
    suggestions = modal.get_autocomplete_suggestions()

    # 항목이 있는지 확인
    assert len(suggestions) > 0

    # 항목에 keyword 단어가 포함되는지 확인(최소 1개 이상)
    matching_list = []
    for auto in suggestions:
        if(keyword in auto):
            matching_list.append(auto)
    
    assert len(matching_list)>=1
    
    print("✅ TC_005 통과: 자동완성 키워드 테스트 성공")
    
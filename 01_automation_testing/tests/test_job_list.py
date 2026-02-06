from pages.job_list_page import JobListPage
import pytest


def test_job_filter_qa(browser, base_url):
    """TC_015: 직군 필터 - 개발 > QA 테스트 엔지니어"""
    
    # 1. /wdlist 페이지로 이동
    browser.get(base_url + "/wdlist")
    job_list_page = JobListPage(browser)
    
    # 2. 페이지 로드 확인
    assert job_list_page.is_loaded(), "채용 공고 페이지 로드 실패"
    
    # 3. 직군·직무 버튼 클릭
    job_list_page.click_job_group_button()
    
    # 4. 대분류 "개발" 선택
    job_list_page.select_category("개발")
    
    # 5. 소분류 "QA 테스트 엔지니어" 선택
    job_list_page.select_job("QA 테스트 엔지니어")
    
    # 6. 적용 버튼 클릭
    job_list_page.apply_filter()
    
    # 7. 검색 결과에 "QA" 키워드가 5개 이상 포함되는지 확인
    assert job_list_page.keyword_in_job_cards("QA"), "QA 필터링 결과 부족"
    
    print("✅ TC_015 통과: 직군 필터 정상 동작")


def test_job_filter_reset(browser, base_url):
    """TC_016: 직군 필터 초기화 기능"""
    
    # 1. /wdlist 페이지로 이동
    browser.get(base_url + "/wdlist")
    job_list_page = JobListPage(browser)
    
    # 2. 페이지 로드 확인
    assert job_list_page.is_loaded(), "채용 공고 페이지 로드 실패"
    
    # 3. 직군·직무 버튼 클릭
    job_list_page.click_job_group_button()
    
    # 4. 대분류 "개발" 선택
    job_list_page.select_category("개발")
    
    # 5. 소분류 "QA 테스트 엔지니어" 선택
    job_list_page.select_job("QA 테스트 엔지니어")
    
    # 6. 적용 버튼 클릭
    job_list_page.apply_filter()
    
    # 7. URL 확인 (필터 적용됨)
    assert "/wdlist/all" not in job_list_page.get_current_url(), "필터가 적용되지 않음"
    
    # 8. 초기화
    job_list_page.click_job_group_button()
    job_list_page.reset_filter()
    job_list_page.apply_filter()
    
    # 9. URL이 초기 상태로 돌아왔는지 확인
    assert "/wdlist/all" in job_list_page.get_current_url(), "필터가 초기화되지 않음"
    
    print("✅ TC_016 통과: 직군 필터 초기화 정상 동작")
from pages.job_detail_page import JobDetailPage
from pages.job_list_page import JobListPage
import pytest

def test_job_detail_page_load(browser, base_url):
    """TC_019: 채용 공고 상세 페이지 로드 확인"""
    
    # 1. 채용 공고 페이지로 이동
    browser.get(base_url+"/wdlist")
    job_list_page = JobListPage(browser)
    assert job_list_page.is_loaded(), "채용 공고 페이지 로드 실패"

    # 2. 첫 번째 채용 공고의 position_id 추출
    first_position_id = job_list_page.get_first_card_position_id()
    assert first_position_id is not None, "첫 번째 채용 공고의 position_id 추출 실패"
    print(f"첫 번째 채용 공고 position_id: {first_position_id}")

    # 3. 첫 번째 채용 공고 클릭하여 상세 페이지로 이동
    job_list_page.go_to_first_job_detail()

    # 4. 채용 공고 상세 페이지 로드 확인
    job_detail_page = JobDetailPage(browser)
    assert job_detail_page.is_loaded(), "채용 공고 상세 페이지 로드 실패"

    # 5. URL에 position_id가 포함되어 있는지 확인
    current_url = job_detail_page.get_current_url()
    assert first_position_id in current_url, "상세 페이지 URL에 position_id가 포함되지 않음"
    print("✅ TC_019 통과: 채용 공고 상세 페이지 정상 로드")

def test_job_description_section(browser,base_url):
    """TC_021 : 채용 공고 상세 - 포지션 상세 섹션 확인"""
    # 1. /wdlist 페이지에서 position_id 추출
    browser.get(base_url + "/wdlist")
    job_list_page = JobListPage(browser)

    position_id = job_list_page.get_first_card_position_id()
    assert position_id is not None, "첫 번째 채용 공고의 position_id 추출 실패"

    # 2. 상세 페이지로 직접 이동
    browser.get(f"{base_url}/wd/{position_id}")
    job_detail_page = JobDetailPage(browser)
    assert job_detail_page.is_loaded(), "채용 공고 상세 페이지 로드 실패"

    # 3. 포지션 상세 확인
    assert job_detail_page.verify_job_description_content(), "포지션 상세 섹션 내용 확인 실패"
    
    # 4. 지도 섹션 확인
    assert job_detail_page.verify_map_section(), "지도 섹션 내용 확인 실패"
    print("✅ TC_021 통과: 채용 공고 상세 - 포지션 상세 섹션 정상 확인")
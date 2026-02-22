# /test/test_main_page.py

import time
from pages.main_page import MainPage
import pytest

# 페이지 로드 확인
def test_page_loaded(browser,base_url):
    browser.get(base_url)
    time.sleep(2)

    main_page = MainPage(browser)
    assert main_page.is_loaded()

@pytest.mark.skip(reason="원티드에서 AI Agent 기능 제거됨 (2025.02.12)")
def test_ai_button_visible(browser,base_url):
    # ai에이전트 버튼 확인 : TC_028
    browser.get(base_url)
    time.sleep(2)

    main_page = MainPage(browser)
    assert main_page.is_element_visible(main_page.AI_SEARCH_BUTTON)

@pytest.mark.skip(reason="원티드에서 AI Agent 기능 제거됨 (2025.02.12)")
def test_ai_agent_button_click(browser,base_url):
    browser.get(base_url)
    time.sleep(2)

    main_page = MainPage(browser)
    main_page.click_ai_agent_button()
    time.sleep(2)

    assert "/ai/agent" in browser.current_url


def test_shortcut_menu_click(browser,base_url):
    # TC_033 :shortcut 바로가기 메뉴 작동 확인
    browser.get(base_url)
    time.sleep(2)

    # 페이지 최상단으로 스크롤
    browser.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)

    main_page = MainPage(browser)
    main_page.click_shortcut_menu("position")
    time.sleep(2)

    assert "/wdlist" in browser.current_url
    print("✅ TC_033 통과: shortcut 바로가기 메뉴 작동 확인")

def test_slider_navigation(browser,base_url):
    """TC_032 : 메인 페이지 슬라이더 작동"""
    browser.get(base_url)
    main_page = MainPage(browser)
    assert main_page.is_loaded(), "메인 페이지 로드 실패"
    time.sleep(2)

    # 1. 첫 슬라이드 제목 저장
    first_titles = main_page.get_visible_card_titles()
    assert len(first_titles) >= 4, "첫 슬라이드 카드 제목 추출 실패"
    print(f"첫 슬라이드 카드 제목: {first_titles}")

    # 2. 오른쪽(다음) 버튼 클릭
    main_page.click_slider_right()
    time.sleep(2)

    # 3. 콘텐츠 변경 확인
    second_titles = main_page.get_visible_card_titles()
    assert first_titles != second_titles, "슬라이더 오른쪽 이동 후 콘텐츠 변경 없음"

    # 4. 왼쪽(이전) 버튼 클릭
    main_page.click_slider_left()
    time.sleep(2)

    # 5. 첫 슬라이드로 복귀 확인
    reverted_titles = main_page.get_visible_card_titles()
    assert first_titles == reverted_titles, "슬라이더 왼쪽 이동 후 첫 슬라이드로 복귀 실패"

    print("✅ TC_032 통과: 메인 페이지 슬라이더 정상 작동")

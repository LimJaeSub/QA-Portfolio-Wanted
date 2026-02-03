# /test/test_main_page.py

import time
from pages.main_page import MainPage

# 페이지 로드 확인
def test_page_loaded(browser,base_url):
    browser.get(base_url)
    time.sleep(2)

    main_page = MainPage(browser)
    assert main_page.is_loaded()

# ai에이전트 버튼 확인
def test_ai_button_visible(browser,base_url):
    browser.get(base_url)
    time.sleep(2)

    main_page = MainPage(browser)
    assert main_page.is_element_visible(main_page.AI_SEARCH_BUTTON)

# ai 에이전트 페이지 이동 확인
def test_ai_agent_button_click(browser,base_url):
    browser.get(base_url)
    time.sleep(2)

    main_page = MainPage(browser)
    main_page.click_ai_agent_button()
    time.sleep(2)

    assert "/ai/agent" in browser.current_url

# shortcut 바로가기 메뉴 작동 확인
def test_shortcut_menu_click(browser,base_url):
    browser.get(base_url)
    time.sleep(2)

    # 페이지 최상단으로 스크롤
    browser.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)

    main_page = MainPage(browser)
    main_page.click_shortcut_menu("position")
    time.sleep(2)

    assert "/wdlist" in browser.current_url

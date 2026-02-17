import time
import pytest
from pages.header_component import Header

# 디버깅
from selenium.webdriver.common.by import By

def test_logo_click(browser,base_url):
    # 로고 클릭시 메인 페이지 이동 : TC_025
    # 다른 페이지에서 시작해야함
    browser.get(base_url+"ai/agent")
    time.sleep(2)

    header = Header(browser)
    header.click_logo()
    time.sleep(2)

    assert browser.current_url == base_url \
        or browser.current_url == base_url + "/"


@pytest.mark.parametrize("menu_kind,expected_url",[
    ("jobs","wdlist"),
    ("event","event"),
    ("resume","cv/intro"),
    ("content","events"),
    ("community","community")
])
def test_menu_click(browser,base_url,menu_kind,expected_url):
    # 메뉴 클릭시 페이지 이동 : TC_026
    browser.get(base_url)
    time.sleep(2)

    header = Header(browser)
    header.click_menu(menu_kind)
    time.sleep(2)

    assert expected_url in browser.current_url

def test_responsive_hamburger_menu(browser, base_url):
    """TC_037: 반응형 - 햄버거 메뉴 992px 기준 확인"""
    
    browser.get(base_url)
    header = Header(browser)
    
    # 1. 1200px - 햄버거 숨김
    browser.set_window_size(1200, 800)
    time.sleep(1)
    width, _ = header.get_window_size()
    assert not header.is_hamburger_menu_visible(), f"{width}px에서 햄버거 보임"
    print(f"✅ {width}px: 햄버거 숨김 확인")
    
    # 2. 991px - 햄버거 보임
    browser.set_window_size(1007, 800)
    time.sleep(1)
    width, _ = header.get_window_size()
    assert header.is_hamburger_menu_visible(), f"{width}px에서 햄버거 안 보임"
    print(f"✅ {width}px (innerWidth:991px): 햄버거 보임 확인")
    
    # 3. 경계값 - 991px (보임)
    browser.set_window_size(1007, 800)
    time.sleep(1)
    assert header.is_hamburger_menu_visible(), "경계값 991px에서 햄버거 안 보임"
    print("✅ 경계값 991px: 햄버거 보임 확인")
    
    # 4. 경계값 - 992px (숨김)
    browser.set_window_size(1008, 800)
    time.sleep(1)
    assert not header.is_hamburger_menu_visible(), "경계값 992px에서 햄버거 보임"
    print("✅ 경계값 992px: 햄버거 숨김 확인")
    
    # 5. 복원
    header.set_desktop_viewport()
    print("✅ TC_037 통과: 반응형 햄버거 메뉴 정상 동작")


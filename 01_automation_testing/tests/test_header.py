import time
import pytest
from pages.header_component import Header

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

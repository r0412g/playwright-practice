from playwright.sync_api import Page, expect


def test_practice_page_opens(page: Page, practice_url):
    page.goto(practice_url)
    expect(page).to_have_title("網頁自動化測試練習場")
    expect(page.locator("#page-title")).to_have_text("網頁自動化測試練習場")
from playwright.sync_api import sync_playwright, expect
from time import sleep


url = 'https://dock.tech/'


def test_dock_homepage():
  with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)

    cookies_accept = page.locator('xpath=//*[@id="onetrust-accept-btn-handler"]')
    cookies_accept.click()
    sleep(1)

    translate_btn = page.locator('xpath=//*[@id="menu-menu-principal"]/div/div/div[1]')
    translate_btn.click()
    english_translation = page.locator('xpath=//*[@id="menu-menu-principal"]/div/div/div[2]/a[1]')
    english_translation.click()

    form filling
    page.locator('xpath=//*[@id="lb-nome"]').fill('Carlos tester')
    page.locator('xpath=//*[@id="PhoneNumber2"]').fill('83999999999')
    page.locator('xpath=//*[@id="lb-email"]').fill('test@dock.com')
    page.locator('xpath=//*[@id="lb-empresa"]').fill('Testing at Dock')
    page.locator('xpath=//*[@id="lb-site"]').fill('http://testing.dock/')
    page.locator('xpath=//*[@id="lb-assunto"]').select_option('SOLUÇÃO - BANKING')

    page.locator('xpath=//*[@id="lb-idioma"]').nth(0).select_option('Inglês')

    page.locator('xpath=//*[@id="lb-msg"]').fill('Hi, there! This is just a testing message, please don`t sue me or be angry with me!')
    page.locator('xpath=//*[@id="wpcf7-f29-o1"]/form/div[2]/div[2]/span/span/span/label/input').click()

    btn_send = page.locator('xpath=//*[@id="wpcf7-f29-o1"]/form/div[2]/div[3]/input')
    expect(btn_send).to_be_visible()
    btn_send.click()

    sleep(10)

    thanks_msg = page.locator('xpath=//*[@id="lb-assunto"]')
    expect(thanks_msg).to_be_visible()

    browser.close()
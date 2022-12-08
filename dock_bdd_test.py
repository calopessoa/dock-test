"""Dock Home Page feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from playwright.sync_api import sync_playwright, expect

url = 'https://dock.tech/'

def test_playwright_bdd_init():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()


        @scenario('features/dock_form.feature', 'Changing the page\'s language to english')
        def _():
            print("Changing the page's language to english.")
            pass


        @scenario('features/dock_form.feature', 'Filling the form and sending it to the team')
        def _():
            print("Filling the form and sending it to the team.")
            pass


        @given('that I`ve accessed the home page')
        def _():
            page.goto(url)


        @given('clicked to accept the cookies')
        def _():
            cookies_accept = page.locator('xpath=//button[@id="onetrust-accept-btn-handler"]')
            cookies_accept.click()


        @when('I click to change the page`s language')
        def _():
            translate_btn = page.locator('xpath=//*[@id="menu-menu-principal"]/div/div/div[1]')
            translate_btn.click()
            english_translation = page.locator('xpath=//*[@id="menu-menu-principal"]/div/div/div[2]/a[1]')
            english_translation.click()


        @then('I see that Dock have more than 69 million active accounts')
        def _():
            active_acc = page.locator('xpath=//*[@id="Wrapper"]/section[2]/div/div/div[1]/h2')
            expect(active_acc).to_contain_text("69")
            expect(active_acc).to_contain_text( " MILLION ACTIVE ACCOUNTS")


        @then('45% CAGR since 2014')
        def _():
            annual_growth_rate = page.locator('xpath=//*[@id="Wrapper"]/section[2]/div/div/div[4]/h2')
            expect(annual_growth_rate).to_contain_text("45%")
            expect(annual_growth_rate).to_contain_text(" CAGR SINCE 2014")


        @when('I fill out all the required forms')
        def _():
            page.locator('xpath=//*[@id="lb-nome"]').fill('Carlos tester')
            page.locator('xpath=//*[@id="PhoneNumber2"]').fill('83999999999')
            page.locator('xpath=//*[@id="lb-email"]').fill('test@dock.com')
            page.locator('xpath=//*[@id="lb-empresa"]').fill('Testing at Dock')
            page.locator('xpath=//*[@id="lb-site"]').fill('http://testing.dock/')
            page.locator('xpath=//*[@id="lb-assunto"]').select_option('SOLUÇÃO - BANKING')

            page.locator('xpath=//*[@id="lb-idioma"]').nth(0).select_option('Inglês')

            page.locator('xpath=//*[@id="lb-msg"]').fill('Hi, there! This is just a testing message, please don`t sue me or be angry with me!')


        @when('I click to send it')
        def _():
            page.locator('xpath=//*[@id="wpcf7-f29-o1"]/form/div[2]/div[2]/span/span/span/label/input').click()
            btn_send = page.locator('xpath=//*[@id="wpcf7-f29-o1"]/form/div[2]/div[3]/input')
            expect(btn_send).to_be_visible()
            btn_send.click()


        @then('I see a message that validates my request')
        def _():
            thanks_msg = page.locator('xpath=//*[@id="lb-assunto"]')
            expect(thanks_msg).to_be_visible()

            browser.close()

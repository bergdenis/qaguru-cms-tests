from selene import browser, be, have


def test_should_find_selene(setup_browser):
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('Selene').press_enter()
    browser.element('#web_content_wrapper').should(have.text('Selene'))


def test_should_not_find_anything(setup_browser):
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('sfgt13jkl57ss').press_enter()
    browser.element('#web_content_wrapper').should(have.text('No results found for sfgt13jkl57ss'))

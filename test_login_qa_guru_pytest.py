from selene import browser, have


def test_valid_login():
    browser.open('https://school.qa.guru')

    browser.element('[name="email"]').type('bergdenis@seznam.cz')
    browser.element('[name="password"]').type('Scouser2005!').press_enter()
    browser.element('body').should(have.text('Полезные ссылки'))

    browser.open('https://school.qa.guru/cms/system/login')
    browser.element('.logined-form').should(have.text('Здравствуйте, Denis'))

    #browser.quit()


def test_wrong_password_login():
    browser.open('https://school.qa.guru')

    browser.element('[name="email"]').type('bergdenis@seznam.cz')
    browser.element('[name="password"]').type('qwerty').press_enter()
    browser.element('.btn-error').should(have.text('Неверный пароль'))


def test_empty_password_login():
    browser.open('https://school.qa.guru')

    browser.element('[name="email"]').type('bergdenis@seznam.cz')
    browser.element('[name="password"]').type('').press_enter()
    browser.element('.btn-error').should(have.text('Не заполнено поле Пароль'))


def test_empty_login():
    browser.open('https://school.qa.guru')

    browser.element('[name="password"]').type('').press_enter()
    browser.element('.btn-error').should(have.text('Не заполнено поле E-Mail'))


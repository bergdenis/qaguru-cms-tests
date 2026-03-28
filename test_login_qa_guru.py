from selene import browser, have

browser.open('https://school.qa.guru')

browser.element('[name="email"]').type('bergdenis@seznam.cz')
browser.element('[name="password"]').type('Scouser2005!').press_enter()

browser.element('body').should(have.text('Полезные ссылки'))

browser.open('https://school.qa.guru/cms/system/login')
browser.element('.logined-form').should(have.text('Здравствуйте, Denis'))

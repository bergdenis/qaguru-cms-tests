from selene import browser, have


def test_fill_practice_form():
    browser.open('/')

    browser.element('#firstName').type('John')
    browser.element('#lastName').type('Doe')
    browser.element('#userEmail').type('test@gmail.com')
    browser.element('#gender-radio-3').click()
    browser.element('#userNumber').type('0012344556')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').send_keys('1977')
    browser.element('.react-datepicker__month-select').send_keys('July')
    browser.element('.react-datepicker__day--007').click()
    browser.element('#subjectsInput').type('Comp')
    browser.element('.subjects-auto-complete__option').click()
    browser.element('#hobbies-checkbox-1').click()
    browser.element('#hobbies-checkbox-2').click()
    browser.element('#currentAddress').type('123 Main St, New York')

    browser.element('#state').click()
    browser.all('[id^=react-select-3-option]').element_by(have.text('NCR')).click()
    browser.element('#city').click()
    browser.all('[id^=react-select-4-option]').element_by(have.text('Delhi')).click()

    browser.element('#submit').click()

    browser.element('.modal-dialog').should(have.text('John'))
    browser.element('.modal-dialog').should(have.text('Doe'))
    browser.element('.modal-dialog').should(have.text('Computer Science'))

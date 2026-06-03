import inspect
from datetime import time


def test_dark_theme_by_time():
    """
    Test that dark theme is enabled correctly based on time of day
    """
    current_time = time(hour=23)
    # TODO: enable dark theme based on time of day (from 22:00 to 06:00 - night time)
    if current_time >= time(hour=22) or current_time <= time(hour=6):
        is_dark_theme = True
    else:
        is_dark_theme = False

    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Test that dark theme switches correctly based on time and user preference.
    dark_theme_enabled_by_user = True - Dark theme is enabled
    dark_theme_enabled_by_user = False - Dark theme is disabled
    dark_theme_enabled_by_user = None - User has not made a choice (system time is used)
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True

    # TODO: switch dark theme based on time of day,
    #  but take into account that dark theme can be enabled manually
    if dark_theme_enabled_by_user is True:
        is_dark_theme = True
    elif dark_theme_enabled_by_user is False:
        is_dark_theme = False
    else:
        if current_time >= time(hour=22) or current_time <= time(hour=6):
            is_dark_theme = True
        else:
            is_dark_theme = False

    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Find the required user by conditions in the list of users
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO: find the user with the name "Olga"
    for user in users:
        if user["name"] == "Olga":
            suitable_users = user

    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO: find all users under 20 years old
    suitable_users = []
    for user in users:
        if user["age"] < 20:
            suitable_users.append(user)

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Create a function that will print a readable name
# of the given function and its argument values.
# Call it inside the functions described below.
# Hint: the function name can be obtained using func.__name__
# For example, calling the following function should convert the function name
# to a more readable format (replace underscores with spaces,
# capitalize the letters), then print all argument values of this function:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def print_function_name_and_args(func, *args):
    func_name = func.__name__.replace('_', ' ').title()
    args_name = ", ".join([*args])
    f"{func_name} [{args_name}]"
    return f"{func_name} [{args_name}]"


def open_browser(browser_name):
    actual_result = print_function_name_and_args(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = print_function_name_and_args(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = print_function_name_and_args(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
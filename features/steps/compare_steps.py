import support.ui as ui
from hamcrest import *


@when("Select product #{index} for compare")
def step(context, index):
    ui.Product(context.browser, index, method='index').add_to_compare()


@then("'{title}' popup should be displayed")
def step(context, title):
    window_name = context.browser.window_handles[-1]
    context.browser.switch_to.window(window_name)

    assert_that(
        context.browser.title,
        starts_with(title))


@when("Close popup")
def step(context):
    context.browser.close()
    context.browser.switch_to.window(
        context.browser.window_handles[0])

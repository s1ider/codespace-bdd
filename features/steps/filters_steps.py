import support.pages as pages
import support.ui as ui
from hamcrest import *


@when("Filter by '{filter_path}'")
def step(context, filter_path):
    filter_category, filter_value = filter_path.split('->')
    pages.LoginPage(context.browser).filter_by(filter_category, filter_value)


@when("Store number of products")
def step(context):
    number = ui.Product(context.browser, '*', method='index').count
    context.scenario.number_of_products = number


@then("Number of products should be less then stored value")
def step(context):
    actual_number = ui.Product(context.browser, '*', method='index').count

    assert_that(
        actual_number,
        less_than(context.scenario.number_of_products))

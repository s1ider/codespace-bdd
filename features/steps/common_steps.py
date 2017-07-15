from behave import given, when, then
import support.ui as ui
import support.pages as pages
import support.utils as utils
from selenium.common.exceptions import NoSuchElementException
from hamcrest import *


@given("I am on '{page}' page")
def step(context, page):
    pages = __import__('support.pages', fromlist=[str(page.lower())])
    pages_class = getattr(pages, page + 'Page')
    pages_class(context.browser).open()


@given("Logged in with {credentials} credentials")
def step(context, credentials):
    if not pages.LoginPage(context.browser).is_logged_in:
        creds = context.settings['credentials'][credentials]
        login, pwd = creds.values()
        page = pages.LoginPage(context.browser)
        page.open()
        page.login(login, pwd)


@when("Fill text form")
def step(context):
    for row in context.table:
        ui.Input(context.browser, row['label']).fill(row['value'])

@when("Fill form")
def step(context):
    for row in context.table:
        element = utils.get_ui_class(row['type'])
        element(context.browser, row['label']).fill(row['value'])


@when("Click on {obj_type} '{obj_name}'")
def step_click(context, obj_type, obj_name):
    cls = utils.get_ui_class(obj_type)
    cls(context.browser, obj_name).click()


@when("Try click on {obj_type} '{obj_name}'")
def step(context, obj_type, obj_name):
    try:
        context.execute_steps(u"""
            when Click on {} '{}'
            """.format(obj_type, obj_name))
    except NoSuchElementException:
        context.logger.warn("Element {} {} not found".format(obj_type, obj_name))
        pass


@then("{obj_type} '{obj_name}' should be displayed")
def step(context, obj_type, obj_name):
    cls = utils.get_ui_class(obj_type)
    assert cls(context.browser, obj_name).is_visible


@when("Fail")
@then("Fail")
@then("Stop")
def step(context):
    assert False


@when("Navigate to '{path}'")
def step(context, path):
    # Header->Link
    header, link = path.split('->')
    ui.Link(context.browser, header).hover()
    ui.Link(context.browser, link).click()


@when("Confirm alert")
def step(context):
    context.browser.switch_to.alert.accept()
    
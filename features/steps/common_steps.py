from behave import given, when, then
import support.ui as ui
import support.utils as utils


@given("I am on '{page}' page")
def step(context, page):
    pages = __import__('support.pages', fromlist=[str(page.lower())])
    pages_class = getattr(pages, page + 'Page')
    pages_class(context.browser).open()


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
def step(context, obj_type, obj_name):
    cls = utils.get_ui_class(obj_type)
    cls(context.browser, obj_name).click()


@then("{obj_type} '{obj_name}' should be displayed")
def step(context, obj_type, obj_name):
    cls = utils.get_ui_class(obj_type)
    assert cls(context.browser, obj_name).is_visible


@when("Fail")
@then("Fail")
@then("Stop")
def step(context):
    assert False

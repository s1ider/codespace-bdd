from behave import given, when, then
import support.pages as pages
import support.ui as ui


@given("I am on 'Login' page")
def step(context):
	pages.LoginPage(context.browser).open()


@when("Fill text form")
def step(context):
	for row in context.table:
		ui.Input(context.browser, row['label']).fill(row['value'])


@when("Click on button '{name}'")
def step(context, name):
	ui.Button(context.browser, name).click()


@then("Header '{name}' should be displayed")
def step(context, name):
	assert ui.Header(context.browser, name).is_visible
	
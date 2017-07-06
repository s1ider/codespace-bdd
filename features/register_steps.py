import support.pages as pages


@then("Success message about registration should be displayed")
def step(context):
    pages.RegistrationPage(context.browser).is_register_success

import support.pages as pages


@when("Filter by '{filter_path}'")
def step(context, filter_path):
    filter_category, filter_value = filter_path.split('->')
    pages.LoginPage(context.browser).filter_by(filter_category, filter_value)
import support.pages as pages
from hamcrest import *


@when("Change qty of product #{index:d} to {qty:d}")
def step(contex, index, qty):
    products = pages.CartPage(contex.browser).products
    products[index + 1].edit_qty(qty)


@then("Verify grand total equals to sum of all prices")
def step(context):
    cart = pages.CartPage(context.browser)
    assert_that(
        sum([product.subtotal for product in cart.products]),
        equal_to(cart.grand_total))

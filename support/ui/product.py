from .base_element import BaseElement


class Product(BaseElement):
    def __init__(self, browser, value, method='name'):
        locator = {
            'name': ('//div[@class="product-info"]'
                     '[h2[@class="product-name"]'
                     '/a[text()="{}"]]'),
            'index': '(//div[@class="product-info"])[{}]'
        }[method].format(value)
        super(Product, self).__init__(browser, locator)

    def select(self):
        loc = './h2[@class="product-name"]/a'
        self.element.find_element_by_xpath(loc).click()

    def add_to_compare(self):
        loc = './/a[text() = "Add to Compare"]'
        self.element.find_element_by_xpath(loc).click()

    def add_to_wishlist(self)
        loc = './/a[text() = "Add to Wishlist"]'
        self.element.find_element_by_xpath(loc).click()

from .base_page import BasePage


class AddressBookPage(BasePage):
    def __init__(self, browser):
        super(AddressBookPage, self).__init__(browser)
        self.url = 'http://magento-demo.lexiconn.com/customer/address/'
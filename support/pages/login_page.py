from .base_page import BasePage
import support.ui as ui


class LoginPage(BasePage):
    def __init__(self, browser):
        # super() calls parent methods
        super(LoginPage, self).__init__(browser)

        base_url = self.settings['base_url']
        self.url = base_url + '/customer/account/login/'
        # locators mappings (css)
        self.locators = {
            'email': '//input[@name="login[username]"]',
            'password': '//input[@name="login[password]"]',
            'login_btn': '//button[@name="send"]',
            'forgot_lnk': '//a[contains(text(), "Forgot Your Password?")]',

            # search
            'search_input': '//input[@id="search"]',
            'search_results': '//div[@id="search_autocomplete"]/ul/li[@title]',

            # login criteria
            'login_criteria': '//a[@title="Log Out"]',
        }

    @property
    def is_logged_in(self):
        return bool(self.find_elements('login_criteria'))

    def login(self, email, pwd):
        email_input = self.find_element('email')
        pwd_input = self.find_element('password')
        email_input.clear()
        email_input.send_keys(email)
        pwd_input.send_keys(pwd)

        self.find_element('login_btn').click()

    def forgot_account(self):
        self.find_element('forgot_lnk').click()

    def search(self, query):
        self.find_element('search_input').send_keys(query)

    def navigate_to(self, path):
        # Header->Link
        header, link = path.split('->')
        ui.Link(self.browser, header).hover()
        ui.Link(self.browser, link).click()

    def filter_by(self, category, name):
        loc_filter = ('//dt[text() = "{0}"]/following-sibling::dd[1]'
                      '//li/a[starts-with(normalize-space(.), "{1}")]'
                      ).format(category, name)

        self.browser.find_element_by_xpath(loc_filter).click()

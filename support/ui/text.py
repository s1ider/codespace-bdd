from .base_element import BaseElement


class Text(BaseElement):
    def __init__(self, browser, text):
        locator = '//span[contains(., "{}")]'.format(text)
        super(Text, self).__init__(browser, locator)

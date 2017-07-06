from selenium import webdriver
import logging


def before_all(context):
    # setup logging
    logging.basicConfig(level=logging.INFO)
    context.logger = logging.getLogger()

    # setup webdriver remotely
    context.logger.debug("setting up WebDriver")
    context.browser = webdriver.Remote('http://127.0.0.1:4444/wd/hub/',
        desired_capabilities=webdriver.DesiredCapabilities.CHROME)
    context.browser.implicitly_wait(1)


def after_all(context):
    if not context.failed:
        context.browser.quit()

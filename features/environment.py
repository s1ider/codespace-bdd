from selenium import webdriver
import logging
import yaml
import os.path


def before_all(context):
    # setup logging
    logging.basicConfig(level=logging.INFO)
    context.logger = logging.getLogger()

    # read settings
    with open('settings.yaml') as f:
        context.settings = yaml.load(f.read())

    # setup webdriver remotely
    context.logger.debug("setting up WebDriver")
    if os.path.exists('browser.session') and context.config.userdata.get('reuse', False):
        with open('browser.session') as f:
            session_id, session_url = f.read().split(' ')
        context.browser = webdriver.Remote(session_url, 
            desired_capabilities=webdriver.DesiredCapabilities.CHROME)
        context.browser.close()
        context.browser.session_id = session_id
    else:
        context.browser = webdriver.Remote('http://127.0.0.1:4444/wd/hub/',
            desired_capabilities=webdriver.DesiredCapabilities.CHROME)
        with open('browser.session', 'w') as f:
            f.write("{0} {1}".format(context.browser.session_id,
                                     context.browser.command_executor._url))

    # context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(1)


def after_scenario(context, scenario):
    if scenario.status == 'failed':
        filename = os.path.join('screenshots', scenario.name + '.png')
        context.browser.save_screenshot(filename)


def after_all(context):
    if not context.failed:
        context.browser.quit()

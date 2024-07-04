import pytest
import os
from appium import webdriver
from appium.options.common.base import AppiumOptions
import dotenv

dotenv.load_dotenv()

@pytest.fixture(scope="function", autouse=True)
def driver():
    """
    This fixture is used to initialize the appium driver
    """
    options = AppiumOptions()

    # change as per your requirement
    options.load_capabilities(
        {
            "platformName": "",
            "appium:deviceName": "",
            "appium:platformVersion": "",
        }
    )

    driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

    # uncomment below code for lambdatest integration
    # for more information visit: https://www.lambdatest.com/support/docs/appium-python-pytest/
    # and for capabilities visit: https://www.lambdatest.com/capabilities-generator/

    # options.load_capabilities({
    #     "platformName": "",
    #     "appium:deviceName": "",
    #     "appium:platformVersion": "",
    #     "appium:app": "",
    #     "appium:autoGrantPermissions": True,
    #     "appium:isRealMobile": True,
    #     "appium:ensureWebviewsHavePages": True,
    #     "appium:nativeWebScreenshot": True,
    #     "lambdatest:source": "appiumdesktop",
    #     "lambdatest:isRealMobile": True,
    #     "appium:newCommandTimeout": 3600,
    #     "appium:connectHardwareKeyboard": True
    # })

    # driver = webdriver.Remote(f"https://{os.getenv('LAMBDATEST_USERNAME')}:{os.getenv('LAMBDATEST_ACCESS_KEY')}@mobile-hub.lambdatest.com/wd/hub", options=options)

    yield driver

    driver.quit()
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.action_helpers import ActionHelpers

# For Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AppiumPage:
    def __init__(self, driver):
        """
        Initialize the AppiumPage with a driver.

        Args:
            driver: The Appium driver instance.
        """
        self.driver = driver

    def installed_app(self, app_id):
        """
        Check if the app is installed on the device.

        Args:
            app_id (str): The app identifier.

        Returns:
            bool: True if the app is installed, False otherwise.
        """
        return self.driver.is_app_installed(app_id)

    def open_app(self, app_id):
        """
        Open the app.

        Args:
            app_id (str): The app identifier.
        """
        self.driver.activate_app(app_id)

    def find_element(self, selector, locator, multiple=False, by_locator=None):
        """
        Locate an element on the page.

        Args:
            selector (str): The selector type to locate the element.
            locator (str): The locator of the element.
            multiple (bool): True if multiple elements are to be located, False otherwise.
            by_locator: Locator to find the element using a custom locator.

        Returns:
            WebElement or list: The found element or list of elements.
        """
        selector_map = {
            "id": AppiumBy.ID,
            "class": AppiumBy.CLASS_NAME,
            "xpath": AppiumBy.XPATH,
            "accessibility_id": AppiumBy.ACCESSIBILITY_ID,
            "android_uiautomator": AppiumBy.ANDROID_UIAUTOMATOR,
            "css": AppiumBy.CSS_SELECTOR,
            "name": AppiumBy.NAME,
            "link_text": AppiumBy.LINK_TEXT,
            "partial_link_text": AppiumBy.PARTIAL_LINK_TEXT,
            "tag_name": AppiumBy.TAG_NAME
        }

        if selector not in selector_map.keys():
            raise ValueError(f"Unsupported selector type: {selector}")
        selector = selector_map[selector]
        if multiple:
            return self.driver.find_elements(selector, value=locator)
        if by_locator:
            return by_locator.find_element(selector, value=locator)
        else:
            return self.driver.find_element(selector, value=locator)

    def get_count_elements(self, by_locator):
        """
        Get the count of elements.

        Args:
            by_locator (list): A list of locators for the elements.

        Returns:
            int: The count of elements.
        """
        return len(by_locator)

    def click(self, by_locator):
        """
        Click on an element on the page.

        Args:
            by_locator: The locator of the element.
        """
        by_locator.click()

    def tap(self, x, y):
        """
        Tap on the screen at the specified coordinates.

        Args:
            x (int): The x-coordinate of the tap.
            y (int): The y-coordinate of the tap.
        """
        action = ActionHelpers(self.driver)
        action.tap(positions=(x, y))

    def send_keys(self, selector, locator, text):
        """
        Send keys to an input field on the page.

        Args:
            selector (str): The selector type to locate the element.
            locator (str): The locator of the input field.
            text (str): The text to be sent.
        """
        element = self.find_element(selector=selector, locator=locator)
        element.send_keys(text)

    def get_title(self):
        """
        Get the title of the page.

        Returns:
            str: The title of the page.
        """
        return self.driver.title

    def clear(self, by_locator):
        """
        Clear the input field on the page.

        Args:
            by_locator: The locator of the element.
        """
        by_locator.clear()

    def property(self, by_locator=None, property_name=None, selector=None, locator=None):
        """
        Extract the specified property from the given Appium locator.

        Args:
            by_locator: The Appium WebElement from which to extract the property.
            property_name (str): The name of the property to extract.
            selector (str, optional): The selector type to locate the element.
            locator (str, optional): The locator of the element.

        Returns:
            The value of the specified property, or None if the property does not exist.
        """
        try:
            if selector and locator and (by_locator is None):
                by_locator = self.find_element(selector, locator)

            if property_name == 'text':
                return by_locator.text
            elif property_name == 'tag_name':
                return by_locator.tag_name
            elif property_name == 'size':
                return by_locator.size
            elif property_name == 'location':
                return by_locator.location
            elif property_name == 'location_in_view':
                return by_locator.location_in_view
            elif property_name == 'rect':
                return by_locator.rect
            elif property_name == 'is_displayed':
                return by_locator.is_displayed()
            elif property_name == 'is_enabled':
                return by_locator.is_enabled()
            elif property_name == 'is_selected':
                return by_locator.is_selected()
            elif property_name == 'get_attribute':
                raise ValueError("For 'get_attribute', provide the attribute name as a third parameter.")
            else:
                raise ValueError(f"Property '{property_name}' is not supported.")
        except Exception as e:
            print(f"Error extracting property '{property_name}': {e}")
            return None

    def attribute(self, by_locator, attribute_name):
        """
        Extract the specified attribute from the given Appium locator.

        Args:
            by_locator: The Appium WebElement from which to extract the attribute.
            attribute_name (str): The name of the attribute to extract.

        Returns:
            The value of the specified attribute, or None if the attribute does not exist.
        """
        try:
            return by_locator.get_attribute(attribute_name)
        except Exception as e:
            print(f"Error extracting attribute '{attribute_name}': {e}")
            return None

    def swipe(self, start_x, start_y, end_x, end_y, duration):
        """
        Swipe from one point to another on the User app.

        Args:
            start_x (int): The starting x-coordinate.
            start_y (int): The starting y-coordinate.
            end_x (int): The ending x-coordinate.
            end_y (int): The ending y-coordinate.
            duration (int): The duration of the swipe in milliseconds.
        """
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def script(self, *args, **kwargs):
        """
        Execute a script on the app.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        self.driver.execute_script(*args, **kwargs)

    def script(self, escript):
        """
        Execute a script on the app.

        Args:
            escript (str): The script to be executed.
        """
        self.driver.execute_script(escript)

    def quit(self):
        """
        Quit the app.
        """
        self.driver.quit()

    def wait_for_element(self, selector, locator, timeout=10):
        """
        Wait for an element to be present on the page.

        Args:
            selector (str): The selector type to locate the element.
            locator (str): The locator of the element.
            timeout (int): The maximum time to wait in seconds.

        Returns:
            bool: True if the element is found within the timeout, False otherwise.
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((selector, locator)))
            return True
        except:
            return self.quit()

    def wait(self, time=5):
        """
        Implicitly wait for a given time.

        Args:
            time (int): The wait time in seconds.
        """
        self.driver.implicitly_wait(time)

from Project.test.fixtures.pages.MainPage import AppiumPage


class UserPage(AppiumPage):
    def __init__(self, driver):
        super().__init__(driver)

    def user_login(self):
        """
        Login Page 
        """
        # wait for element
        self.wait(time=10)
        # permission button
        permission = self.find_element(selector="id", locator="")
        self.click(permission) # Click on the permission button YES
        # wait for element
        self.wait(5)
        # enter email for user login
        self.send_keys(selector="android_uiautomator", locator="")
        # enter password for user login
        self.send_keys(selector="android_uiautomator", locator="", text="init1234")
        # click on the login button
        login_button = self.find_element(selector="accessibility_id", locator="loginid")
        self.click(login_button)
        # wait for element
        self.wait(time=10)

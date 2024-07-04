import pytest
from Project.test.pages.Users.userPage import UserPage

@pytest.fixture
def user_page(driver):
    return UserPage(driver)

@pytest.mark.usefixtures("driver")
class TestUserPage:
    """
    Test cases for the User Page
    """
    def test_login(self, user_page):
        """
        This test case checks if the user can login
        """
        user_page.user_login()

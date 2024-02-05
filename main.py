from testcase.test_login import TestLogin
from playwright.sync_api import Page


if __name__ == "__main__":
    test = TestLogin(Page)
    test.main()

from playwright.sync_api import sync_playwright
from tools.csv_reader import csv_data, CsvReader
from page.login_page import LoginPage


class TestLogin(LoginPage):
    csv_get_data = CsvReader()
    home = "https://192.168.10.172"

    def setup(self):
        self.p = sync_playwright().start()
        self.browser = self.p.chromium.launch(channel="chrome", headless=False, args=["--start-maximized"])
        self.context = self.browser.new_context(no_viewport=True, ignore_https_errors=True)
        self.page = self.context.new_page()
        super().__init__(self.page)
        self.goto_login(self.home)

    # @pytest.mark.parametrize("username,password,assertion,url", csv_data)
    @csv_data("username,password,assertion,url,method", csv_get_data)
    def test_login(self, row):
        self.fill_username(value=row['username'])
        self.fill_password(row['password'])
        self.code = self.ocr_rec()
        self.fill_verify_code(self.code)
        if not self._ele_is_checked(self._info_protection):
            self.click_info()
        self.click_login_button()
        more_page = self.context.new_page()
        more_page.goto(row['url'])
        self._ele_to_be_visible(row['method'], row['assertion'])
        self.click_button_logout()
        more_page.close()

    def teardown(self):
        self.context.close()
        self.browser.close()
        self.page.close()
        # self.p.stop()

    def main(self):
        self.setup()
        self.test_login()
        self.teardown()

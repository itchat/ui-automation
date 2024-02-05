from base.base import Base
from tools.captcha import Cap


class LoginPage(Base, Cap):
    _username = '#username'
    _password = '#password'
    _verify_space = "#vrifyCode"
    _login_button = "#login-btn"
    _verify_path = r"data\captcha.png"
    _info_protection = "#protocalBtn"
    _verify_img = "#Kaptcha"
    _logout_button = "xpath=//a[contains(text(),'退出')]"

    def __init__(self, page):
        super().__init__(page)

    def goto_login(self, url):
        try:
            self._goto_url(url)
        except Exception as e:
            print(f"Error navigating to {url}: {e}")
            raise

    def fill_username(self, value):
        # self._click(self._username)
        self._fill(self._username, value)

    def fill_password(self, value):
        self._fill(self._password, value)

    def fill_verify_code(self, value):
        self._fill(self._verify_space, value)

    def click_info(self):
        self._click(self._info_protection)

    def click_login_button(self):
        self._click(self._login_button)

    def click_button_logout(self):
        self._click(self._logout_button)

    def browser_operation(self, reload=True, forward=False, back=False):
        self._browser_operation(reload=reload, forward=forward, back=back)

    def ocr_rec(self):
        p = self.screenshot(path=self._verify_path, full_page=False, locator=self._verify_img)
        code = self.recognition(p)
        return code

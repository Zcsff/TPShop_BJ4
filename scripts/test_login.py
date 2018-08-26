from base.base_driver import init_driver
from page.page import Page


class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_login(self):
        self.page.home_page.click_my()
        self.page.mine_page.click_login_sign_up()
        self.page.login_page.input_username("13800138006")
        self.page.login_page.input_password("123456")
        self.page.login_page.click_login()

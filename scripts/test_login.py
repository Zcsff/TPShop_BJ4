from time import sleep

import allure
import pytest
from allure.constants import AttachmentType
from selenium.webdriver.common.by import By
import random

from base.base_analyze import analyze_with_file

from base.base_driver import init_driver
from page.page import Page


# 八位的密码:
def random_password():
    password = ""
    for i in range(8):
        password += str(random.randint(0, 9))
    return password


def show_password_data():
    password_list = list()
    for i in range(2):
        password_list.append(random_password())
    return password_list


class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    # @pytest.mark.parametrize("argsname", analyze_with_file("login_data", "test_login"))
    # def test_login(self, argsname):
    #     username = argsname["username"]
    #     password = argsname["password"]
    #     expect = argsname["expect"]
    #
    #     self.page.home_page.click_my()
    #     self.page.mine_page.click_login_sign_up()
    #     self.page.login_page.input_username(username)
    #     self.page.login_page.input_password(password)
    #     self.page.login_page.click_login()
    #     assert self.page.login_page.is_toast_exist(expect)

    @pytest.mark.parametrize("argsname", analyze_with_file("login_data", "test_login_miss_part"))
    def test_login_miss_part(self, argsname):
        username = argsname["username"]
        password = argsname["password"]

        self.page.home_page.click_my()
        self.page.mine_page.click_login_sign_up()
        self.page.login_page.input_username(username)
        self.page.login_page.input_password(password)
        assert not self.page.login_page.is_longin_enabled()
    # @pytest.mark.parametrize("password", show_password_data())
    # def test_show_password(self, password):
    #     password_feature = By.XPATH, "//*[@text='%s']" % password
    #     self.page.home_page.click_my()
    #     self.page.mine_page.click_login_sign_up()
    #     self.page.login_page.input_password(password)
    #     assert not self.page.login_page.is_location_exist(password_feature)
    #     self.page.login_page.click_show_password()
    #     # 截图,在报告中显示,如果想保存在本地,可以使用之前的截图方式
    #     sleep(2)
    #     allure.attach("显示密码", self.driver.get_screenshot_as_png(), AttachmentType.PNG)
    #     assert self.page.login_page.is_location_exist(password_feature)

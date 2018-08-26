import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    usename_edit_button = By.ID, "com.tpshop.malls:id/edit_phone_num"
    password_edit_button = By.ID, "com.tpshop.malls:id/edit_password"
    login_button = By.ID, "com.tpshop.malls:id/btn_login"

    @allure.step(title="输入用户名")
    def input_username(self, text):
        allure.attach("用户名是:", text)
        self.input(self.usename_edit_button, text)

    @allure.step(title="输入密码:")
    def input_password(self, text):
        allure.attach("密码是:", text)
        self.input(self.password_edit_button, text)

    @allure.step(title="点击登录")
    def click_login(self):
        self.click(self.login_button)
from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    FORM_LOGIN_EMAIL = (By.ID, "id_login-username")
    FORM_LOGIN_PASS = (By.ID, "id_login-password")
    FORM_REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    FORM_REGISTRATION_PASS = (By.ID, "id_registration-password1")
    FORM_REGISTRATION_CONFIRM_PASS = (By.ID, "id_registration-password2")

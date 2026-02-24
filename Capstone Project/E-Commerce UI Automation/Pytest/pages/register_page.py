from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegisterPage(BasePage):

    MALE_GENDER = (By.ID, "gender-male")
    FEMALE_GENDER = (By.ID, "gender-female")

    FIRSTNAME = (By.ID, "FirstName")
    LASTNAME = (By.ID, "LastName")
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    CONFIRM_PASSWORD = (By.ID, "ConfirmPassword")
    REGISTER_BUTTON = (By.ID, "register-button")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "result")

    def __init__(self, driver, logger=None):
        super().__init__(driver, logger)

    def select_gender(self, gender):
        gender = gender.lower()

        if gender == "male":
            self.click(self.MALE_GENDER, "Male Gender Radio Button")
        elif gender == "female":
            self.click(self.FEMALE_GENDER, "Female Gender Radio Button")
        else:
            raise ValueError(f"Invalid gender value in CSV: {gender}")

        if self.logger:
            self.logger.info(f"Gender selected: {gender}")

    def register_user(self, fname, lname, email, password, gender):
        self.select_gender(gender)

        self.enter_text(self.FIRSTNAME, fname, "First Name Field")
        self.enter_text(self.LASTNAME, lname, "Last Name Field")
        self.enter_text(self.EMAIL, email, "Email Field")
        self.enter_text(self.PASSWORD, password, "Password Field")
        self.enter_text(self.CONFIRM_PASSWORD, password, "Confirm Password Field")

        self.click(self.REGISTER_BUTTON, "Register Button")

        if self.logger:
            self.logger.info("Registration form submitted")

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE, "Registration Success Message")

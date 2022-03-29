class LoginForm:
    LOGIN_URL = "https://stage-tody.sptech.team/auth/login"
    LOGIN_FIELD_XPATH = ".//input[@type='text' and @name='_username']"
    PASSWORD_FIELD_XPATH = ".//input[@type='password' and @name='_password']"
    SIGN_IN_BUTTON_XPATH = ".//button[@type='submit']"
    ERROR_MESSAGE_TEXT = "An authentication exception occurred."
    ERROR_MESSAGE_XPATH = ".//div[@class='alert alert-danger']"
    H1_XPATH = ".//h1[@class='h1 mb-0']"

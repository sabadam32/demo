from pages.utility.common import Driver
from pages.utility.accounts import Accounts


class Home:
    '''Home page object'''

    def __init__(self) -> None:

        self._url = "/"
        self.page = Driver.page
        
        self.username = self.page.locator("[data-test='username']")
        self.password = self.page.locator("[data-test='password']")
        self.login = self.page.locator("[data-test='login-button']")
        self.error = self.page.locator("[data-test='error']")

        self._load()
        
    def _load(self) -> None:
        if self.page.url != f"{Driver.base_url}{self._url}":
            self.page.goto(f"{Driver.base_url}{self._url}")
        
    def _login(self, username: str, password: str) -> None:
        self.username.fill(username)
        self.password.fill(password)
        self.login.click()

    def login_as_standard_user(self) -> None:
        self._login(Accounts.STANDARD_USER, Accounts.DEFAULT_PASSWORD)

    def login_as_locked_out_user(self) -> None:
        self._login(Accounts.LOCKED_OUT_USER, Accounts.DEFAULT_PASSWORD)

    def login_as_problem_user(self) -> None:
        self._login(Accounts.PROBLEM_USER, Accounts.DEFAULT_PASSWORD)

    def login_as_performance_glitch_user(self) -> None:
        self._login(Accounts.PERFORMANCE_GLITCH_USER, Accounts.DEFAULT_PASSWORD)

    def login_as_error_user(self) -> None:
        self._login(Accounts.ERROR_USER, Accounts.DEFAULT_PASSWORD)

from pages.utility import Driver, Accounts
from pages.utility.exceptions import LoginException
from playwright.sync_api import TimeoutError
from warnings import warn


class Home:
    """Home page object"""

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

        try:
            self.page.wait_for_url(f"**/inventory.html", timeout=5000)
        except TimeoutError:
            if self.error.is_visible():
                raise LoginException(
                    f"Login Error: {self.error.inner_text()}"
                ) from None
            else:
                warn(
                    "Login Warning: Page did not redirect to inventory.html after 5 seconds."
                )

                # Continue to wait until normal timeout in case it is just slow.
                self.page.wait_for_url(f"**/inventory.html", timeout=10000)

    def login_with(self, account: str, password=Accounts.DEFAULT_PASSWORD) -> None:
        self._login(account, password)

    def validate_login_with(self, account: str, password: str) -> None:
        self.username.fill(account)
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

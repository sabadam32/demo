from pages.utility.common import Driver


class Cart:
    """Cart page object"""

    def __init__(self) -> None:

        self._url = "/cart.html"
        self.page = Driver.page

        self.checkout = self.page.locator("[data-test='checkout']")
        self.continue_shopping = self.page.locator("[data-test='continue-shopping']")

        self._load()

    def _load(self) -> None:
        if self.page.url != f"{Driver.base_url}{self._url}":
            self.page.goto(f"{Driver.base_url}{self._url}")

    def item_in_cart(self, item_name: str) -> bool:
        return self.page.get_by_text(item_name).is_visible()

    def go_to_checkout(self) -> None:
        self.checkout.click()

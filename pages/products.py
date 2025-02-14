from typing import Self
from pages.utility import Driver, Inventory
from pages.utility.exceptions import CartException
from playwright.sync_api import expect


class Products:
    """Products page object"""

    def __init__(self) -> None:

        self._url = "/inventory.html"
        self.page = Driver.page

        self.shopping_cart = self.page.locator("[data-test='shopping-cart-link']")
        self.item_count = self.page.locator("[data-test='shopping-cart-badge']")
        self.error = self.page.locator("[data-test='error']")
        self._load()

    def _load(self) -> None:
        if self.page.url != f"{Driver.base_url}{self._url}":
            self.page.goto(f"{Driver.base_url}{self._url}")

    def _add_item(self, item) -> None:
        current_count = (
            self.item_count.inner_text() if self.item_count.is_visible() else 0
        )
        self.page.locator(f"[data-test='{item.locator}']").click()
        try:
            expect(self.item_count).to_contain_text(
                f"{int(current_count) + 1}", timeout=100
            )
        except AssertionError:
            raise CartException(
                f"Error Adding {item.name} to Cart: Count is {current_count} but should be {current_count + 1}"
            ) from None

    def add_backpack_to_cart(self):
        self._add_item(Inventory.Backpack)
        return self

    def add_bike_light_to_cart(self) -> Self:
        self._add_item(Inventory.BikeLight)
        return self

    def add_shirt_to_cart(self) -> Self:
        self._add_item(Inventory.BoltTShirt)
        return self

    def add_fleece_to_cart(self) -> Self:
        self._add_item(Inventory.FleeceJacket)
        return self

    def add_onesie_to_cart(self) -> Self:
        self._add_item(Inventory.Onesie)
        return self

    def add_red_tshirt_to_cart(self) -> Self:
        self._add_item(Inventory.TShirtRed)
        return self

    def go_to_cart(self) -> Self:
        self.shopping_cart.click()
        return self

    def get_item_count(self) -> int:
        return int(self.item_count.inner_text())

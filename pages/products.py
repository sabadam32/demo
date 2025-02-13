from typing import Self
from pages.utility.common import Driver
from pages.utility.inventory import Inventory


class Products:
    '''Products page object'''

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
        self.page.locator(f"[data-test='{item}']").click()

    def add_backpack_to_cart(self):
        self._add_item(Inventory.Backpack.locator)
        return self

    def add_bike_light_to_cart(self) -> Self:
        self._add_item(Inventory.BikeLight.locator)
        return self
    
    def add_shirt_to_cart(self) -> Self:
        self._add_item(Inventory.BoltTShirt.locator)
        return self

    def add_fleece_to_cart(self) -> Self:
        self._add_item(Inventory.FleeceJacket.locator)
        return self
    
    def add_onesie_to_cart(self) -> Self:
        self._add_item(Inventory.Onesie.locator)
        return self

    def add_red_tshirt_to_cart(self) -> Self:
        self._add_item(Inventory.TShirtRed.locator)
        return self

    def go_to_cart(self) -> Self:
        self.shopping_cart.click()
        return self

    def get_item_count(self) -> int:
        return int(self.item_count.inner_text())
    
from pages.utility.common import Driver
from pages.utility.user_info import UserInfo
from typing import Self
import time

class Checkout:
    '''Checkout page object'''

    def __init__(self) -> None:

        self._url = "/checkout-"
        self.page = Driver.page
        
        self.first_name = self.page.locator("[data-test='firstName']")
        self.last_name = self.page.locator("[data-test='lastName']")
        self.zip = self.page.locator("[data-test='postalCode']")
        self.continue_checkout = self.page.locator("[data-test='continue']")
        self.finish = self.page.locator("[data-test='finish']")
        self.back_home = self.page.locator("[data-test='back-to-products']")
        self.complete_message = self.page.locator("[data-test='complete-header']")

        self.error = self.page.get_by_test_id('error')

        self._load()
        
    def _load(self) -> None:
        if self._url not in self.page.url:
            self.page.goto(f"{Driver.base_url}{self._url}")
        
    def as_user(self, first_name: str, last_name: str, zip: str) -> Self:
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.zip.fill(zip)
        self.continue_checkout.click()
        return self

    def finish_checkout(self) -> Self:
        self.finish.click()
        return self
        
    def get_message(self) -> str:
        return self.complete_message.inner_text()
    
    def successful_checkout(self) -> None:
        return self.as_user(*UserInfo.TEST_USER).finish_checkout().get_message()

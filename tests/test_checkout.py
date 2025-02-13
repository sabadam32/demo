from pages import (
    Cart,
    Checkout,
    Home,
    Products
)
from pages.utility.common import Driver
from pages.utility.inventory import Inventory
from playwright.sync_api import Page, expect
import pytest


@pytest.fixture()
def set_up(page: Page):
    Driver.set_base_url('https://www.saucedemo.com')
    Driver.set_driver(page)
    yield

    Driver.page.close()


def test_happy_path_checkout(set_up):
    Home().login_as_standard_user()

    Products().add_backpack_to_cart().go_to_cart()
    assert Cart().item_in_cart(Inventory.Backpack.name)

    Cart().go_to_checkout()
    assert Checkout().successful_checkout() == 'Thank you for your order!'


@pytest.mark.xfail
def test_failed_add_to_cart(set_up):
    Home().login_as_error_user()

    Products().add_shirt_to_cart().go_to_cart()
    assert Cart().item_in_cart(Inventory.BoltTShirt.name), 'Is Item in cart'

    Cart().go_to_checkout()
    assert Checkout().successful_checkout() == 'Thank you for your order!'


def test_must_login_to_shop(set_up):
    expect(Products().error).to_contain_text("Epic sadface: You can only access '/inventory.html' when you are logged in")


def test_happy_path_cart(set_up):
    Home().login_as_standard_user()

    assert Products().add_backpack_to_cart().get_item_count() == 1
    assert Cart().item_in_cart(Inventory.Backpack.name)

    Cart().go_to_checkout()
    assert Checkout().successful_checkout() == 'Thank you for your order!'

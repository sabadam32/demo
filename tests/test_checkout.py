from pages import Cart, Checkout, Home, Products
from pages.utility import Driver, Inventory, Accounts, UserInfo
from playwright.sync_api import Page, expect
import pytest


@pytest.fixture(scope="function", autouse=True)
def set_up(page: Page):
    page.set_default_timeout(10000)
    Driver.base_url = "https://www.saucedemo.com"
    Driver.page = page
    yield

    Driver.page.close()


@pytest.mark.parametrize(
    "account",
    [
        Accounts.STANDARD_USER,
        Accounts.LOCKED_OUT_USER,
        Accounts.PROBLEM_USER,
        Accounts.PERFORMANCE_GLITCH_USER,
        Accounts.ERROR_USER,
        Accounts.VISUAL_USER,
    ],
)
def test_happy_path_checkout(account):
    """Validate that the user can add an item to the cart and checkout"""

    Home().login_with(account)

    # Ensure the item is indicated as added to the cart
    Products().add_backpack_to_cart()
    assert Products().get_item_count() == 1

    # Ensure that the item is in the cart
    Products().go_to_cart()
    assert Cart().item_in_cart(Inventory.Backpack.name)

    # Ensure a successful checkout.
    Cart().go_to_checkout()
    assert Checkout().complete_checkout() == "Thank you for your order!"


def test_must_login_to_shop():
    expect(Products().error).to_contain_text(
        "Epic sadface: You can only access '/inventory.html' when you are logged in"
    )


def test_must_enter_user_information():
    Home().login_as_standard_user()
    Products().go_to_cart()
    Cart().go_to_checkout()
    Checkout().as_user("", "", "")
    assert "First Name is required" in Checkout().error.inner_text()

    Checkout().as_user(UserInfo.TestUser.first_name, "", "")
    assert "Last Name is required" in Checkout().error.inner_text()

    Checkout().as_user(UserInfo.TestUser.first_name, UserInfo.TestUser.last_name, "")
    assert "Postal Code is required" in Checkout().error.inner_text()

    Checkout().as_user(
        UserInfo.TestUser.first_name, UserInfo.TestUser.last_name, UserInfo.TestUser.zip
    )
    assert Driver.page.url == f"{Driver.base_url}/checkout-step-two.html"


def test_cannot_bypass_user_information_step():
    Home().login_as_standard_user()
    Products().go_to_cart()
    Cart().go_to_checkout()

    # Skip the user information and navigate directly to the second step
    Driver.page.goto(f"{Driver.base_url}/checkout-step-two.html")
    Checkout().finish_checkout()

    # Should not be able to bypass required information
    assert (
        Driver.page.url != f"{Driver.base_url}/checkout-complete.html"
    ), "Error: Bypassed user information step."


def test_valid_postal_code():
    Home().login_as_standard_user()
    Products().go_to_cart()
    Cart().go_to_checkout()
    Checkout().as_user(
        UserInfo.TestUser.first_name, UserInfo.TestUser.last_name, "WeeHah!"
    )
    assert (
        Driver.page.url != f"{Driver.base_url}/checkout-step-two.html"
    ), "Error: Invalid postal code was accepted."


def test_input_length():
    Home().login_as_standard_user()
    Products().go_to_cart()
    Cart().go_to_checkout()

    # Generate a string of 100 characters
    Checkout().as_user("a" * 100, "b" * 100, "c" * 100)
    assert Checkout().error.is_visible(), "Error: Input fields do not have limits."


def test_username_and_password_required():
    Home().validate_login_with("", "")
    assert "Username is required" in Home().error.inner_text()

    Home().validate_login_with(Accounts.STANDARD_USER, "")
    assert "Password is required" in Home().error.inner_text()


def test_password_case_sensitive():
    Home().validate_login_with(Accounts.STANDARD_USER, "SeCrEt_sAuCe")
    assert (
        "Username and password do not match any user in this service"
        in Home().error.inner_text()
    )


def test_username_case_sensative():
    Home().validate_login_with(
        Accounts.STANDARD_USER.upper(), Accounts.DEFAULT_PASSWORD
    )
    assert (
        "Username and password do not match any user in this service"
        in Home().error.inner_text()
    )


def test_no_clue_given_for_invalid_credentials():
    Home().validate_login_with(Accounts.STANDARD_USER, "password")
    assert (
        "Username and password do not match any user in this service"
        in Home().error.inner_text()
    )
    Home().validate_login_with("babblefish", Accounts.DEFAULT_PASSWORD)
    assert (
        "Username and password do not match any user in this service"
        in Home().error.inner_text()
    )

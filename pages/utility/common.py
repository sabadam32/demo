from playwright.sync_api import Page


class Driver:
    """This will hold objects used by the whole framework"""

    page: Page = None
    base_url: str = None

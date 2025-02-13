from playwright.sync_api import Page


class Driver:
    '''This will hold objects used by the whole framework'''

    page: Page = None
    base_url: str = None

    @classmethod
    def set_driver(cls, page: Page) -> None:
        cls.page = page
        cls.page.set_default_timeout(3000)

    @classmethod
    def set_base_url(cls, url) -> None:
        cls.base_url = url
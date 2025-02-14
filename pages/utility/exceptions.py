class LoginException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class CartException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

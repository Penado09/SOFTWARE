from account import Account

class Driver(Account):
    def __init__(self, name, document,
    email, password):
        super().__init__(name,
        document, email, password)